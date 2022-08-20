import json
from yellowbrick.cluster import KElbowVisualizer
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

import os
import logging
import time
import psycopg2

import pandas as pd
from sqlalchemy import create_engine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
from functools import lru_cache

def connect_postgres():
    database = os.environ['POSTGRES_DB']
    user = os.environ['POSTGRES_USER']
    password = os.environ['POSTGRES_PASSWORD']
    host = os.environ['POSTGRES_SERVER']
    port = 5432

    exc, conn, engine = None, None, None

    for _ in range(5):
        try:
            conn = psycopg2.connect(
                database=database,
                user=user,
                password=password,
                host=host,
                port=port
            )
        except Exception as e:
            logging.warning(
                "Error connecting to postgres, will retry in 3 sec: %s", e
            )
            time.sleep(3)
            exc = e
        else:
            logging.info("Connected...")
            logging.info(
                "Everything goes well from Postgres, you're a fu*** pro..."
            )

            engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(
                user, password, host, port, database
            ))
            break
    else:
        logging.error("Unable to connect to  %s DB", database)
        raise exc

    return [conn, engine]

# TODO: activate cache
@lru_cache(maxsize=32)
def kmeans(program_code, sede_code, jornada_code):
    [conn, engine] = connect_postgres()

    df_iss = pd.read_sql("""
        SELECT
            copytransaction.id,
            code,
            title_name,
            trans_copy_code_id,
            trans_tittle_code_id,
            trans_date_id as date_iss
        FROM
            public.copytransaction,
            public.transactiontype,
            public.copy,
            public.student,
            public.date,
            public.title
        WHERE
            sede = {sede_code} AND
            jornada = '{jornada_code}' AND
            program = '{program_code}' AND
            trans_type_code IN ('ISS') AND
            trans_tittle_code_id = title.id AND
            trans_date_id = date.id AND
            trans_copy_code_id = copy.id AND
            trans_borrower_code = student.id AND
            trans_type_id = transactiontype.id

        ORDER BY
            code,
            trans_copy_code_id,
            trans_date_id,
            trans_type_code,
            copy.id,
            title_name

    """.format(
        sede_code=sede_code,
        jornada_code=jornada_code,
        program_code=program_code
    ), con=conn)

    df_ret = pd.read_sql("""
        SELECT
            trans_copy_code_id,
            trans_tittle_code_id,
            code,
            title_name,
            trans_date_id as date_ret
        FROM
            public.copytransaction,
            public.transactiontype,
            public.copy,
            public.student,
            public.date,
            public.title
        WHERE
            sede = {sede_code} AND
            jornada = '{jornada_code}' AND
            program = '{program_code}' AND
            trans_type_code IN ('RET') AND
            trans_tittle_code_id = title.id AND
            trans_date_id = date.id AND
            trans_copy_code_id = copy.id AND
            trans_borrower_code = student.id AND
            trans_type_id = transactiontype.id

        ORDER BY
            code,
            trans_copy_code_id,
            trans_date_id,
            trans_type_code,
            title_name

    """.format(
        sede_code=sede_code,
        jornada_code=jornada_code,
        program_code=program_code
    ), con=conn)

    if df_iss.empty and df_ret.empty:
        return []

    df_iss = df_iss.reset_index(drop=True)
    df_ret = df_ret.reset_index(drop=True)

    df_iss = df_iss.astype(
        {col: 'int32' for col in df_iss.select_dtypes('int64').columns}
    )

    df_ret = df_ret.astype(
        {col: 'int32' for col in df_ret.select_dtypes('int64').columns}
    )

    df = df_iss.merge(
        df_ret,
        how='left',
        on=[
            'code',
            'trans_copy_code_id',
            'trans_tittle_code_id',
            'title_name'
        ]
    )

    df['diff'] = df['date_ret'] - df['date_iss']
    df = df[df['diff'] >= 0]
    df = df.sort_values(
        ['trans_tittle_code_id', 'diff']
    )

    df['ISS'] = pd.to_datetime(df['date_iss'].astype(str), format='%Y%m%d')
    df['RET'] = pd.to_datetime(df['date_ret'].astype(str), format='%Y%m%d')
    df['trans_copy_code_id'] = df['trans_copy_code_id'].astype(str)
    df['trans_tittle_code_id'] = df['trans_tittle_code_id'].astype(str)
    df['duration'] = df['RET'] - df['ISS'] + pd.Timedelta(days=1)
    df['duration'] = df['duration'].dt.days

    # the limit of a duratiohn is 100 days
    df = df[df['duration'] <= 100].sort_values('duration')

    df_titles = df[['trans_tittle_code_id', 'title_name']]
    df_titles = df_titles.set_index('trans_tittle_code_id')
    df_titles

    df_new = df.drop([
        'code',
        'trans_copy_code_id',
        'date_iss',
        'id',
        'date_ret',
        'diff',
        'ISS',
        'RET',
        'title_name'
    ],
        axis=1
    )

    df_new = df_new.groupby(['trans_tittle_code_id'])['duration'].agg(
        borrow_days='sum',
        borrow_numbers='count'
    ).sort_values(
        ['borrow_days', 'borrow_numbers']
    ).reset_index()

    df_new['score'] = df_new['borrow_days'] * df_new['borrow_numbers']
    df_new = df_new.set_index('trans_tittle_code_id')

    columns = df_new.columns
    data_to_standardize = df_new[columns]
    scaler = StandardScaler().fit(data_to_standardize)

    # Standardize the columns.
    standardized_data = df_new.copy()
    standardized_columns = scaler.transform(data_to_standardize)
    standardized_data[columns] = standardized_columns

    km = KMeans(init='k-means++', random_state=540)
    visualizer = KElbowVisualizer(km, k=(1, 10))
    visualizer.fit(standardized_data)

    # Train a Kmeans instance
    n_clusters = visualizer.elbow_value_

    kmeans = KMeans(n_clusters=n_clusters, init='k-means++', random_state=540)
    kmeans.fit(standardized_data)
    clusters = kmeans.predict(standardized_data)
    df_new['cluster'] = clusters

    df_new = df_new.astype(
        {col: 'float' for col in df_new.select_dtypes('int64').columns}
    )

    df_new = df_new.astype(
        {col: 'float' for col in df_new.select_dtypes('float64').columns}
    )

    df_new = df_new.astype(
        {col: 'bool' for col in df_new.select_dtypes('bool').columns}
    )

    df_final = pd.merge(
        df_new, df_titles, on=['trans_tittle_code_id']
    ).drop_duplicates()

    response = []

    for i in range(0, n_clusters):
        df = df_final[df_final['cluster'] == i].sort_values(
            'score', ascending=False
        ).head(20)

        json_response = json.loads(
            df[[
                'score',
                'borrow_days',
                'borrow_numbers',
                'title_name'
            ]].reset_index().to_json(
                orient='records', index=True
            )
        )

        response.append({
            "cluster": i,
            "data": json_response,
            "max": df['score'].max(),
            "min": df['score'].min()
        })

    return response

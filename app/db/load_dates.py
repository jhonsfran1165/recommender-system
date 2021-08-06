import datetime

from sqlalchemy.orm import Session

from app import crud, schemas
from app.utils import read_in_chunks
from app.db import base  # noqa: F401

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def load_dates(db: Session) -> None:
    chunk_iter = read_in_chunks("etl/date_dimension.csv", header=0, sep='*')

    for chunk in chunk_iter:
        for index, row in chunk.iterrows():
            try:
                id = int(row['key'])
            except ValueError:
                print("The id of the date is not an integer... skipping", row['key'])

            date_db = crud.date.get(db, id=id)

            if not date_db:
                date = datetime.datetime.strptime(row['Date'], "%Y-%m-%d").date()
                date_format = str(row['Date_format'])
                day_week = int(row['Day_Week'])
                day_name = str(row['Day_Name'])
                day_month = int(row['Day_Month'])
                day_year = int(row['Day_Year'])
                month = int(row['Month'])
                month_name = str(row['Month_Name'])
                month_number_days = int(row['Days_in_Month'])
                week = int(row['Week'])
                quarter = int(row['Quarter'])
                year = int(row['Year'])
                semester = int(row['Semeter'])

                try:
                    date_in = schemas.DateCreate(
                        id=id,
                        date=date,
                        date_format=date_format,
                        day_week=day_week,
                        day_name=day_name,
                        day_month=day_month,
                        day_year=day_year,
                        month=month,
                        month_name=month_name,
                        month_number_days=month_number_days,
                        week=week,
                        quarter=quarter,
                        year=year,
                        semester=semester
                    )
                    date_in_db = crud.date.create(db, obj_in=date_in)  # noqa: F841
                except:
                    print("There was an error inserting the date", id)
                    raise

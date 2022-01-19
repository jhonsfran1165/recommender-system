from datetime import datetime

from sqlalchemy.orm import Session

from app import crud, schemas
from app.utils import read_in_chunks
from app.db import base  # noqa: F401

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def load_copy_transactions(db: Session) -> None:
    chunk_iter = read_in_chunks("etl/copytrans_modified.csv", header=0, sep='*')

    # TRANDATE	CTRANTP	BORCODE	LOCATION	TITLENO	COPYNO	DELETED

    for chunk in chunk_iter:
        for index, row in chunk.iterrows():
            try:

                trans_date_id = int(datetime.strptime(
                    row['TRANDATE'], "%d/%m/%y"
                ).strftime("%Y%m%d"))

                trans_type = str(row['CTRANTP'])
                trans_location = str(row['LOCATION'])
                trans_title = int(row['TITLENO'])
                trans_copy = int(row['COPYNO'])
                trans_borrower_deleted = int(row['DELETED'])

                trans_borrower = int(row['BORCODE'])

                if (trans_borrower > 0000000 and trans_borrower < 2300000):
                    trans_borrower = int('20' + str(row['BORCODE']))
                elif (trans_borrower > 9000000 and trans_borrower < 9999999):
                    trans_borrower = int('19' + str(row['BORCODE']))
                elif (trans_borrower > 8000000 and trans_borrower < 8999999):
                    trans_borrower = int('18' + str(row['BORCODE']))

                trans_type  = crud.transaction_type.get_by_code(
                    db,
                    trans_type_code=trans_type
                )

                trans_location  = crud.location.get_by_location_code(
                    db,
                    location_code=trans_location
                )

                trans_title = crud.title.get(db, id=trans_title)
                trans_copy = crud.copy.get(db, id=trans_copy)
                trans_borrower = crud.student.get_by_student_code(db, code=trans_borrower)

                # TODO: transform to int but before check if None
                print(
                    trans_type,
                    trans_title,
                    trans_copy,
                    trans_location,
                    trans_borrower
                )

                print(
                    type(trans_type),
                    type(trans_title),
                    type(trans_copy),
                    type(trans_location),
                    type(trans_borrower)
                )

                if (
                    trans_date_id is not None and
                    trans_type is not None and
                    trans_title is not None and
                    trans_copy is not None and
                    trans_location is not None and
                    trans_borrower is not None and
                    trans_borrower_deleted is not None
                ):
                    try:
                        copytrans_in = schemas.CopyTransactionCreate(
                            trans_date_id=trans_date_id,
                            trans_type_id=trans_type.id,
                            trans_borrower_code=trans_borrower.id,
                            trans_location_code_id=trans_location.id,
                            trans_tittle_code_id=trans_title.id,
                            trans_copy_code_id=trans_copy.id,
                            trans_borrower_deleted=trans_borrower_deleted
                        )

                        copytrans_in_db = crud.copy_transaction.create(db, obj_in=copytrans_in)  # noqa: F841

                        print("Copy trans added", trans_title)

                    except Exception as inst:
                        print("There was an error inserting the Copy trans", inst)
                        raise

            except ValueError as error:
                print("The transaction can't be transformed... skipping", error)


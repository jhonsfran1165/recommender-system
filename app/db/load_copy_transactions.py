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

                print(
                    type(row['TRANDATE'])
                )
                trans_date_id = datetime.strptime(
                    row['TRANDATE'], "%d/%m/%y"
                ).date()

                # trans_type = str(row['CTRANTP'])
                # trans_borrower = str(row['BORCODE'])
                # trans_location = str(row['LOCATION'])
                # trans_title = str(row['TITLENO'])
                # trans_copy = str(row['COPYNO'])

                print(
                    trans_date_id,
                    # trans_type,
                    # trans_borrower,
                    # trans_location,
                    # trans_title,
                    # trans_copy
                )

            except ValueError as error:
                print("The transaction can't be transformed... skipping", error)

            # transaction_type  = crud.transaction_type.get_by_code(
            #                         db,
            #                         trans_type_code=trans_type_code
            #                     )

            # if not transaction_type:
            #     trans_type_description = str(row['ctrantpld'])
            #     try:
            #         transaction_type_in = schemas.TransactionTypeCreate(
            #             trans_type_code=trans_type_code,
            #             trans_type_description=trans_type_description,
            #         )
            #         transaction_type = crud.transaction_type.create(db, obj_in=transaction_type_in)  # noqa: F841
            #     except:
            #         print("There was an error inserting the transaction_type", trans_type_code)
            #         raise

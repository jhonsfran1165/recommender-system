from sqlalchemy.orm import Session

from app import crud, schemas
from app.utils import read_in_chunks
from app.db import base  # noqa: F401

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def load_transaction_type(db: Session) -> None:
    chunk_iter = read_in_chunks("etl/transaction_type_modified.csv", header=0, sep='*')

    # data sample
    # ctrantp                                                                                 TRANF
    # ctrantpld                                                        Transferencia Préstamo Desde

    for chunk in chunk_iter:
        for index, row in chunk.iterrows():
            try:
                trans_type_code = str(row['ctrantp'])
            except ValueError:
                print("The trans_type_code of the type is not an string... skipping", row['ctrantp'])

            transaction_type  = crud.transaction_type.get_by_code(
                                    db,
                                    trans_type_code=trans_type_code
                                )

            if not transaction_type:
                trans_type_description = str(row['ctrantpld'])
                try:
                    transaction_type_in = schemas.TransactionTypeCreate(
                        trans_type_code=trans_type_code,
                        trans_type_description=trans_type_description,
                    )
                    transaction_type = crud.transaction_type.create(db, obj_in=transaction_type_in)  # noqa: F841
                except:
                    print("There was an error inserting the transaction_type", trans_type_code)
                    raise

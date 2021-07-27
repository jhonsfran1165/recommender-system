from sqlalchemy.orm import Session

from app import crud, schemas
from app.utils import read_in_chunks
from app.db import base  # noqa: F401

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def load_locations(db: Session) -> None:
    chunk_iter = read_in_chunks("etl/locations_modified.csv", header=0, sep='*')

    # data sample
    # LOC                                                                                   EDU
    # LOCLD                                      Centro Doc. CENDOPU - Inst. Educación y Pedago

    for chunk in chunk_iter:
        for index, row in chunk.iterrows():
            try:
                location_code = str(row['LOC'])
            except ValueError:
                print("The location_code is not an string... skipping", row['LOC'])
            except:
                raise("There is an error")


            location  = crud.location.get_by_location_code(
                                    db,
                                    location_code=location_code
                                )


            if not location:
                location_name = str(row['LOCLD'])
                try:
                    location_in = schemas.LocationCreate(
                        location_code=location_code,
                        location_name=location_name,
                    )
                    location = crud.location.create(db, obj_in=location_in)  # noqa: F841
                except:
                    print("There was an error inserting the location", location_code)
                    raise

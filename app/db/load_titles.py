from sqlalchemy.orm import Session

from app import crud, schemas
from app.utils import read_in_chunks
from app.db import base  # noqa: F401

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def load_titles(db: Session) -> None:
    chunk_iter = read_in_chunks("etl/titles_modified.csv", header=0, sep='*')

    # data sample
    # TITLENO                                                                                 58199
    # TITLE                                                               Nuclear radiation physics
    # SUBTITLE                                                            Nuclear radiation physics

    for chunk in chunk_iter:
        for index, row in chunk.iterrows():
            try:
                id = int(row['TITLENO'])
            except ValueError:
                print("The id of the title is not an integer... skipping", row['TITLENO'])

            title = crud.title.get(db, id=id)

            if not title:
                title_name = str(row['TITLE'])
                subtitle = str(row['SUBTITLE'])
                try:
                    title_in = schemas.TitleCreate(
                        id=id,
                        title_name=title_name,
                        subtitle=subtitle,
                    )
                    title = crud.title.create(db, obj_in=title_in)  # noqa: F841
                except:
                    print("There was an error inserting the title", id)
                    raise

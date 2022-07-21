from sqlalchemy.orm import Session

from app import crud, schemas
from app.utils import read_in_chunks
from app.db import base  # noqa: F401


def load_copies(db: Session) -> None:
    chunk_iter = read_in_chunks("etl/copies_modified.csv", header=0, sep='*')

    # data sample
    # C.COPYNO                                             58199
    # T.TITLENO        38959
    # C.TITLE                          Nuclear radiation physics
    # T.MEDIUM          IMPR
    # A.SNAMEDECODE(A.FNAME,NULL,NULL,,A.FNAME)        Lapp, Ralph Eugene
    # T.PRCLASSMARK    QC173
    # C.SHELFMARKQC173 L316n
    # C.BARCODE     112492.0
    # L.LOCLD  Biblioteca Mario Carvajal - Melendez - Cali. U...

    for chunk in chunk_iter:
        for index, row in chunk.iterrows():
            try:
                id = int(row['C.COPYNO'])
            except ValueError:
                print(
                    "The id of the copy is not an integer... skipping",
                    row['C.COPYNO']
                    )

            copy = crud.copy.get(db, id=id)

            if not copy:
                title_id = int(row['T.TITLENO'])
                copy_title = str(row['C.TITLE'])
                medium_type = str(row['T.MEDIUM'])
                author_name = str(
                    row['A.SNAMEDECODE(A.FNAME,NULL,NULL,,A.FNAME)']
                )
                pr_classmark = str(row['T.PRCLASSMARK'])
                shelfmark = str(row['C.SHELFMARK'])
                bar_code = str(row['C.BARCODE'])
                location = str(row['L.LOCLD'])
                try:
                    copy_in = schemas.CopyCreate(
                        id=id,
                        title_id=title_id,
                        copy_title=copy_title,
                        medium_type=medium_type,
                        author_name=author_name,
                        pr_classmark=pr_classmark,
                        shelfmark=shelfmark,
                        bar_code=bar_code,
                        location=location
                    )
                    copy = crud.copy.create(db, obj_in=copy_in)  # noqa: F841
                except Exception as e:
                    print("There was an error inserting the title", id)
                    raise e

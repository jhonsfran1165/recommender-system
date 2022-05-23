from sqlalchemy.orm import Session

from app import crud, schemas
from app.utils import read_in_chunks
from app.db import base  # noqa: F401

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def load_rules(db: Session) -> None:
    chunk_iter = read_in_chunks("etl/association_rules.csv", header=0, sep='*')

    # -- data sample --
    # antecedents
    # consequents
    # antecedent support
    # consequent support
    # support
    # confidence
    # lift
    # leverage
    # conviction

    for chunk in chunk_iter:
        for index, row in chunk.iterrows():
            try:
                id = int(index)
            except ValueError:
                print(
                    "The id of the copy is not an integer... skipping",
                    index
                )

            rule = crud.rule.get(db, id=id)

            if not rule:
                antecedents_id = int(row['antecedents'])
                consequents_id = int(row['consequents'])
                antecedent_support = float(row['antecedent support'])
                consequent_support = float(row['consequent support'])
                support = float(row['support'])
                confidence = float(row['confidence'])
                lift = float(row['lift'])
                leverage = float(row['leverage'])
                conviction = float(row['conviction'])

                try:
                    rule_in = schemas.RuleCreate(
                        id=id,
                        antecedents_id=antecedents_id,
                        consequents_id=consequents_id,
                        antecedent_support=antecedent_support,
                        consequent_support=consequent_support,
                        support=support,
                        confidence=confidence,
                        lift=lift,
                        leverage=leverage,
                        conviction=conviction
                    )
                    rule = crud.rule.create(db, obj_in=rule_in)  # noqa: F841
                except Exception as e:
                    print(e)
                    print("There was an error inserting the title", id)
                    raise


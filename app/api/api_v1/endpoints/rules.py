import json
from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import engine

from app.api import deps

router = APIRouter()


@router.get("/rules")
def rules(
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Retrieve items.
    """
    data = engine.execute("SELECT * FROM rule LIMIT 10")
    # result = db.session.execute('SELECT * FROM my_table WHERE my_column = :val', {'val': 5})
    result = []

    for r in data:
        # print(r[0]) # Access by positional index
        r_dict = dict(r.items()) # convert to dict keyed by column names
        # print(r_dict)
        result.append(r_dict)

    # TODO: return results rules as json
    print(json.load(result))
    return json.load(result)

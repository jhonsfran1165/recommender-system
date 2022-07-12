
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import json
from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from supertokens_python.recipe.session.framework.fastapi import verify_session
from supertokens_python.recipe.session import SessionContainer

from app import crud, schemas
from app.api import deps
from app.views.rules.kmeans import kmeans

import meilisearch

router = APIRouter()

client = meilisearch.Client('http://recommender-search:7700', "asd7687asdasdkjhwrdf97fcsadfs")

@router.get("/rules", response_model=List[schemas.Rule])
async def rules(
    *,
    db: Session = Depends(deps.get_db),
    session: SessionContainer = Depends(verify_session(session_required=False)),
    id: int,
) -> Any:
    """
    Retrieve rule.
    """
    rules = crud.rule.get_by_antecedent(db, antecedents_id=id)
    return rules


@router.get("/rule", response_model=schemas.Rule)
async def get_rules_by_id(
    *,
    db: Session = Depends(deps.get_db),
    session: SessionContainer = Depends(verify_session(session_required=False)),
    id: int
) -> Any:
    """
    Retrieve rule.
    """
    rule = crud.rule.get(db, id=id)

    return rule


@router.get("/kmeans")
async def get_kmeans(
    *,
    db: Session = Depends(deps.get_db),
    session: SessionContainer = Depends(verify_session(session_required=False))
) -> Any:
    """
    Retrieve kmeans.
    """
    # TODO: use info session to set this up
    result = kmeans(
        program_code=3743,
        sede_code=0,
        jornada_code="DIU"
    )

    json_compatible_item_data = jsonable_encoder(result)
    return JSONResponse(content=json_compatible_item_data)

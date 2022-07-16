from typing import Any, List

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from supertokens_python.recipe.session.framework.fastapi import verify_session
from supertokens_python.recipe.session import SessionContainer

from app import crud, schemas
from app.api import deps
from app.views.rules.kmeans import kmeans

router = APIRouter()


@router.get("/rules", response_model=List[schemas.Rule])
async def rules(
    *,
    db: Session = Depends(deps.get_db),
    session: SessionContainer = Depends(verify_session(session_required=True)),
    id: int,
    confidence: float,
    lift: float
) -> Any:
    """
    Retrieve rules.
    """
    rules = crud.rule.get_by_antecedent(
        db,
        antecedents_id=id,
        confidence=confidence,
        lift=lift
    )
    return rules


@router.get("/kmeans")
async def get_kmeans(
    *,
    db: Session = Depends(deps.get_db),
    session: SessionContainer = Depends(verify_session(session_required=True)),
    prog: int,
    jor: str,
    sede: int
) -> Any:
    """
    Retrieve kmeans.
    """
    # TODO: use info session to set this up
    result = kmeans(
        program_code=prog,
        sede_code=sede,
        jornada_code=jor
    )

    json_compatible_item_data = jsonable_encoder(result)
    return JSONResponse(content=json_compatible_item_data)

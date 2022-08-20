from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core.exceptions import ModelError404

from supertokens_python.recipe.session.framework.fastapi import verify_session
from supertokens_python.recipe.session import SessionContainer

router = APIRouter()


@router.get(
    "/copy",
    response_model=schemas.Copy,
    responses={404: {"model": ModelError404}}
)
def get_copy(
    *,
    db: Session = Depends(deps.get_db),
    session: SessionContainer = Depends(verify_session(session_required=True)),
    id: int = Query(default=1, description="copy id"),
) -> Any:
    """
    Retrieve copy by id.
    """
    copy = crud.copy.get(db, id=id)

    if copy is None:
        raise HTTPException(status_code=404, detail="Copy not found")

    return copy


@router.get(
    "/copies-by-title",
    response_model=List[schemas.Copy],
    responses={404: {"model": ModelError404}}
)
async def get_copies_by_title(
    *,
    db: Session = Depends(deps.get_db),
    session: SessionContainer = Depends(verify_session(session_required=True)),
    id: int = Query(default=1, description="title id"),
) -> Any:
    """
    Retrieve copies.
    """
    copies = crud.copy.get_by_title(db, title_id=id)

    if copies is None or len(copies) == 0:
        raise HTTPException(status_code=404, detail="Copies not found")

    return copies

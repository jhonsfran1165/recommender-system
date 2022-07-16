from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps

from supertokens_python.recipe.session.framework.fastapi import verify_session
from supertokens_python.recipe.session import SessionContainer

router = APIRouter()


@router.get("/copy", response_model=schemas.Copy)
def get_copy(
    *,
    db: Session = Depends(deps.get_db),
    session: SessionContainer = Depends(verify_session(session_required=True)),
    id: int
) -> Any:
    """
    Retrieve copy.
    """
    copy = crud.copy.get(db, id=id)

    return copy


@router.get("/copies-by-title", response_model=List[schemas.Copy])
async def get_copies_by_title(
    *,
    db: Session = Depends(deps.get_db),
    session: SessionContainer = Depends(verify_session(session_required=True)),
    id: int
) -> Any:
    """
    Retrieve copies.
    """
    copies = crud.copy.get_by_title(db, title_id=id)

    return copies

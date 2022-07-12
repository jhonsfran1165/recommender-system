from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/copy", response_model=schemas.Copy)
def copy(
    *,
    db: Session = Depends(deps.get_db),
    # current_user: models.User = Depends(deps.get_current_active_user),
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
    id: int
) -> Any:
    """
    Retrieve copies.
    """
    copies = crud.copy.get_by_title(db, title_id=id)

    return copies

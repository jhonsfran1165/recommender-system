from typing import Any

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

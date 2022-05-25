from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/rules", response_model=List[schemas.Rule])
def rules(
    *,
    db: Session = Depends(deps.get_db),
    # current_user: models.User = Depends(deps.get_current_active_user),
    id: int,
) -> Any:
    """
    Retrieve rule.
    """
    rules = crud.rule.get_by_antecedent(db, antecedents_id=id)

    return rules

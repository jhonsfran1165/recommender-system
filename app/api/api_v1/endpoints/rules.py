import json
from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/rules", response_model=List[schemas.Rule])
def rules(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve rule.
    """

    # rule = crud.rule.get_multi(db, skip=skip, limit=limit)
    rules = crud.rule.get_by_antecedent(db, antecedents_id=434760)


    # if crud.user.is_superuser(current_user):
    #     rule = crud.rule.get_multi(db, skip=skip, limit=limit)
    # else:
    #     rule = crud.rule.get_multi(
    #         db=db, owner_id=current_user.id, skip=skip, limit=limit
    #     )

    return rules

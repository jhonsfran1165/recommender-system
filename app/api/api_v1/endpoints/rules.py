from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from supertokens_python.recipe.session.framework.fastapi import verify_session
from supertokens_python.recipe.session import SessionContainer
from supertokens_python.recipe.emailpassword.asyncio import get_user_by_id

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


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
    user_id = session.get_user_id()
    user_data = await get_user_by_id(user_id)
    print("user_data", user_data)
    rules = crud.rule.get_by_antecedent(db, antecedents_id=id)

    return rules


@router.get("/rule", response_model=schemas.Rule)
async def like_comment(
    *,
    db: Session = Depends(deps.get_db),
    session: SessionContainer = Depends(verify_session(session_required=False)),
    id: int
) -> Any:
    """
    Retrieve rule.
    """
    user_id = session.get_user_id()

    print(user_id)
    rule = crud.rule.get(db, id=id)

    return rule

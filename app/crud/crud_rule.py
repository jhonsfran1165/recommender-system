
from typing import List, TypeVar, Any

from app.crud.base import CRUDBase
from app.models import Rule, Copy
from app.schemas import RuleCreate, RuleUpdate
from sqlalchemy.orm import Session, selectinload


from app.db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)

# TODO: check this out
class CRUDRules(CRUDBase[Rule, RuleCreate, RuleUpdate]):
    def get_by_antecedent(self, db: Session, antecedents_id: int) -> List[ModelType]:
        return db.query(self.model).filter(self.model.antecedents_id == antecedents_id).all()





rule = CRUDRules(Rule)

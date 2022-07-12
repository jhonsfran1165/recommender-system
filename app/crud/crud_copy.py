
from typing import List, TypeVar, Any

from app.crud.base import CRUDBase
from app.models import Copy
from app.schemas import CopyCreate, CopyUpdate

from sqlalchemy.orm import Session, selectinload

from app.db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)


class CRUDCopy(CRUDBase[Copy, CopyCreate, CopyUpdate]):
    def get_by_title(self, db: Session, title_id: int) -> List[ModelType]:
        return db.query(self.model).filter(self.model.title_id == title_id).all()


copy = CRUDCopy(Copy)

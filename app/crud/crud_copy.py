from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.copy import Copy
from app.schemas.copy import CopyCreate, CopyUpdate

# TODO: check this out
class CRUDCopy(CRUDBase[Copy, CopyCreate, CopyUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: CopyCreate, owner_id: int
    ) -> Copy:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[Copy]:
        return (
            db.query(self.model)
            .filter(Copy.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


copy = CRUDCopy(Copy)

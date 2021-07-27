from app.crud.base import CRUDBase
from app.models import Location
from app.schemas import LocationCreate, LocationUpdate

from typing import Any, Optional, TypeVar
from sqlalchemy.orm import Session
from app.db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)

class CRUDLocation(CRUDBase[Location, LocationCreate, LocationUpdate]):
    def get_by_location_code(self, db: Session, location_code: Any) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.location_code == location_code).first()



location = CRUDLocation(Location)

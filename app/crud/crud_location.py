from app.crud.base import CRUDBase
from app.models import Location
from app.schemas import LocationCreate, LocationUpdate


class CRUDLocation(CRUDBase[Location, LocationCreate, LocationUpdate]):
    pass


location = CRUDLocation(Location)

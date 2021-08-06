from app.crud.base import CRUDBase
from app.models import Date
from app.schemas import DateCreate, DateUpdate


class CRUDDate(CRUDBase[Date, DateCreate, DateUpdate]):
    pass


date = CRUDDate(Date)

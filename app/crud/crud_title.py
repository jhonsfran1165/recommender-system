from app.crud.base import CRUDBase
from app.models import Title
from app.schemas import TitleCreate, TitleUpdate


class CRUDTitle(CRUDBase[Title, TitleCreate, TitleUpdate]):
    pass


title = CRUDTitle(Title)

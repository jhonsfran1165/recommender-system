from app.crud.base import CRUDBase
from app.models import Copy
from app.schemas import CopyCreate, CopyUpdate


# TODO: check this out
class CRUDCopyTransaction(CRUDBase[Copy, CopyCreate, CopyUpdate]):
    pass


copy = CRUDCopy(Copy)
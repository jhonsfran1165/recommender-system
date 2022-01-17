from app.crud.base import CRUDBase
from app.models import CopyTransaction
from app.schemas import CopyCreate, CopyUpdate


# TODO: check this out
class CRUDCopyTransaction(CRUDBase[CopyTransaction, CopyCreate, CopyUpdate]):
    pass


copy_transaction = CRUDCopyTransaction(CopyTransaction)

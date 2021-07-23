from app.crud.base import CRUDBase
from app.models import TransactionType
from app.schemas import TransactionTypeCreate, TransactionTypeUpdate


class CRUDTransactionType(CRUDBase[TransactionType, TransactionTypeCreate, TransactionTypeUpdate]):
    pass


transaction_type = CRUDTransactionType(TransactionType)

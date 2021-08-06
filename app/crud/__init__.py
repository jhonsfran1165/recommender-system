from .crud_user import user
from .crud_copy import copy
from .crud_title import title
from .crud_transaction_type import transaction_type
from .crud_location import location
from .crud_date import date

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)

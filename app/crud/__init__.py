from .crud_copy import copy
from .crud_title import title
from .crud_transaction_type import transaction_type
from .crud_location import location
from .crud_date import date
from .crud_student import student
from .crud_copy_transactions import copy_transaction
from .crud_rule import rule

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)

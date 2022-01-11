from sqlalchemy import Column, Integer, String

from app.db.base_class import Base
from app.db.mixin_class import CommonColumnsMixin


class TransactionType(Base, CommonColumnsMixin):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    trans_type_code = Column(String, unique=True, index=True, doc="Transaction code type", comment="Transaction code type")
    trans_type_description = Column(String, doc="Transaction description type", comment="Transaction description type")

    def __str__(self):
        return self.id
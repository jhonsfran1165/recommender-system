from sqlalchemy import Column, Integer, String

from app.db.base_class import Base
from app.db.mixin_class import CommonColumnsMixin

# TODO: map transactions table
class Transaction(Base, CommonColumnsMixin):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    trans_code = Column(String, primary_key=True, index=True, doc="Transaction code type", comment="Transaction code type")
    trans_description = Column(String, doc="Transaction description type", comment="Transaction description type")

    def __str__(self):
        return self.id
from sqlalchemy import Column, Integer, String

from app.db.base_class import Base
from app.db.mixin_class import CommonColumnsMixin


class Location(Base, CommonColumnsMixin):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    location_code = Column(String, index=True, primary_key=True, doc="Location code", comment="Location code")
    location_name = Column(String, nullable=False, doc="Location name", comment="Location name")

    def __str__(self):
        return self.id
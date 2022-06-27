from sqlalchemy import Column, Integer, String

from app.db.base_class import Base
from app.db.mixin_class import CommonColumnsMixin


class Title(Base, CommonColumnsMixin):
    id = Column(Integer, primary_key=True, index=True)

    title_name = Column(
        String,
        index=True,
        nullable=False,
        doc="Name of the title",
        comment="Name of the title"
    )

    subtitle = Column(
        String,
        index=True,
        doc="Subtitle of the title",
        comment="Subtitle of the title"
    )

    def __str__(self):
        return str(self.id)

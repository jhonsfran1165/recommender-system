from sqlalchemy import Column, Integer, String

from app.db.base_class import Base
from app.db.mixin_class import CommonColumnsMixin


class Copy(Base, CommonColumnsMixin):
    id = Column(Integer, primary_key=True, index=True)
    copy_title = Column(String, index=True, nullable=False, doc="Title of the copy", comment="Title of the copy")

    title_id = Column(
        Integer,
        index=True,
        nullable=False,
        doc="Title ID of the copy. Many copy are created from a Title",
        comment="Title ID of the copy. Many copy are created from a Title"
    )

    medium_type = Column(String, doc="Media type of the copy", comment="Media type of the copy")
    author_name = Column(String, doc="Author of the Copy", comment="Author of the Copy")

    pr_classmark = Column(
        String,
        doc="Information about the copy (library data)",
        comment="Information about the copy (library data)"
    )

    shelfmark = Column(
        String,
        doc="Shelf information (library data)",
        comment="Shelf information (library data)"
    )

    bar_code = Column(
        String,
        doc="Bar code of the copy  (library data)",
        comment="Bar code of the copy  (library data)"
    )

    location = Column(
        String,
        doc="Library where the copy is located",
        comment="Library where the copy is located"
    )

    # TODO: is it necessary to add owner user?

    def __str__(self):
        return self.id
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.db.mixin_class import CommonColumnsMixin


# TODO: map transactions table with matriculados information
class CopyTransaction(Base, CommonColumnsMixin):
    id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )

    trans_date_id = Column(
        Integer,
        ForeignKey('date.id'),
        primary_key=True,
        index=True,
        doc="Date of transaction",
        comment="Date of transaction"
    )

    trans_type_id = Column(
        Integer,
        ForeignKey('transactiontype.id'),
        index=True,
        doc="Transaction code type",
        comment="Transaction code type"
    )

    # TODO; create a borrower table and add foreing key
    trans_borrower_code = Column(
        Integer,
        index=True,
        doc="Borrower code",
        comment="Borrower code"
    )

    trans_location_code_id = Column(
        Integer,
        ForeignKey('location.id'),
        index=True,
        doc="Location Code",
        comment="Location Code"
    )

    trans_tittle_code_id = Column(
        Integer,
        ForeignKey('title.id'),
        index=True,
        doc="Title Code",
        comment="Title Code"
    )

    trans_copy_code_id = Column(
        Integer,
        ForeignKey('copy.id'),
        index=True,
        doc="Copy code",
        comment="Copy code"
    )

    trans_borrower_deleted = Column(
        Integer,
        doc="Whether if the borrower was deleted or not",
        comment="Whether if the borrower was deleted or not"
    )

    trans_date = relationship("Date")
    trans_type = relationship("TransactionType")
    trans_location_code = relationship("Location")
    trans_tittle_code = relationship("Title")
    trans_copy_code = relationship("Copy")

    def __str__(self):
        return self.id

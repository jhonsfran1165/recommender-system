from typing import TYPE_CHECKING
from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.db.mixin_class import CommonColumnsMixin

if TYPE_CHECKING:
    from app.models import Copy  # noqa: F401

class Rule(Base, CommonColumnsMixin):
    id = Column(Integer, primary_key=True, index=True)

    antecedents_id = Column(
        Integer,
        ForeignKey('copy.id'),
        index=True,
        nullable=False,
        doc="antecedents",
        comment="antecedents"
    )

    consequents_id = Column(
        Integer,
        ForeignKey('copy.id'),
        index=True,
        nullable=False,
        doc="consequents",
        comment="consequents"
    )

    antecedent_support = Column(
        Float,
        doc="antecedent support",
        comment="antecedent support"
    )

    consequent_support = Column(
        Float,
        doc="Author of the Copy",
        comment="Author of the Copy"
    )

    support = Column(
        Float,
        doc="support",
        comment="support"
    )

    confidence = Column(
        Float,
        doc="confidence",
        comment="confidence"
    )

    lift = Column(
        Float,
        doc="lift",
        comment="lift"
    )

    leverage = Column(
        Float,
        doc="leverage",
        comment="leverage"
    )

    conviction = Column(
        Float,
        doc="conviction",
        comment="conviction"
    )

    antecedents = relationship(
        "Copy",
        foreign_keys=[antecedents_id],
        back_populates="antecedents"
    )

    consequents = relationship(
        "Copy",
        foreign_keys=[consequents_id],
        back_populates="consequents"
    )

    def __str__(self):
        return str(self.id)

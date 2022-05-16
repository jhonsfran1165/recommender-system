from sqlalchemy import Column, Integer, Float

from app.db.base_class import Base
from app.db.mixin_class import CommonColumnsMixin


class Rule(Base, CommonColumnsMixin):
    id = Column(Integer, primary_key=True, index=True)

    antecedents = Column(
        Integer,
        index=True,
        nullable=False,
        doc="antecedents",
        comment="antecedents"
    )

    consequents = Column(
        Integer,
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

    def __str__(self):
        return str(self.id)

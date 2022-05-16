from app.crud.base import CRUDBase
from app.models import Rule
from app.schemas import RuleCreate, RuleUpdate


# TODO: check this out
class CRUDRules(CRUDBase[Rule, RuleCreate, RuleUpdate]):
    pass


rule = CRUDRules(Rule)

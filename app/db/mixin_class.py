from datetime import datetime
from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declarative_mixin


# useful mixins https://gist.github.com/techniq/5174410
@declarative_mixin
class CommonColumnsMixin:
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

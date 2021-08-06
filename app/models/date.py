from sqlalchemy import Column, Integer, String, Date

from app.db.base_class import Base
from app.db.mixin_class import CommonColumnsMixin


class Date(Base, CommonColumnsMixin):
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, index=True, nullable=False, doc="Date dimension time", comment="Date dimension time")
    date_format = Column(String, index=True, nullable=False, doc="Date String dimension time", comment="Date String dimension time")
    day_week = Column(Integer, nullable=False, doc="Number day of the week", comment="Number day of the week")
    day_name = Column(String, nullable=False, doc="Name of the Day", comment="Name of the Day")
    day_month = Column(Integer, nullable=False, doc="Number day of the month", comment="Number day of the month")
    day_year = Column(Integer, nullable=False, doc="Number Day of the year", comment="Number Day of the year")
    month = Column(Integer, nullable=False, doc="Number of the month", comment="Number of the month")
    month_name = Column(String, nullable=False, doc="Name of the Month", comment="Name of the Month")
    month_number_days = Column(Integer, nullable=False, doc="How many days has this month", comment="How many days has this month")
    week = Column(Integer, nullable=False, doc="Week of the year", comment="Week of the year")
    quarter = Column(Integer, nullable=False, doc="Quarter of the year", comment="Quarter of the year")
    year = Column(Integer, nullable=False, doc="Year of the year", comment="Year of the year")
    semester = Column(Integer, nullable=False, doc="Semester of the year", comment="Semester of the year")

    def __str__(self):
        return self.id
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Float,
    Date,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Expense(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    expense_date = Column(Date)
    account = Column(Text)

#Index('my_index', Expense.name, unique=True, mysql_length=255)

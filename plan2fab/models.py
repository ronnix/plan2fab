from pyramid.security import (
    Allow,
    Everyone,
)

from sqlalchemy import (
    Column,
    )

from sqlalchemy.dialects.postgresql import (
        BOOLEAN,
        DATE,
        ENUM,
        INTEGER,
        TEXT,
        TIME,
        TIMESTAMP,
        VARCHAR
        )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
        scoped_session,
        sessionmaker,
        )

from zope.sqlalchemy import ZopeTransactionExtension


DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class RootFactory(object):

    __acl__ = [
            (Allow, Everyone, 'view'),
            (Allow, 'group:editors', 'edit'),
            ]

    def __init__(self, request):
        pass


class Project(Base):

    __tablename__ = 'projects'

    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR, nullable=False, unique=True)
    description = Column(TEXT)
    duration = Column(INTEGER)
    plan = Column(VARCHAR)
    furnitures = Column(TEXT)
    authors = Column(VARCHAR)
    history = Column(TEXT)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    def __init__(self, name):
        self.name = namE


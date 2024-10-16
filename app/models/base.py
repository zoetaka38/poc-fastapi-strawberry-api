import logging
from datetime import datetime

from sqlalchemy import TIMESTAMP, Column, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from app.datetime import utcnow

logger = logging.getLogger(__name__)

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}


class Base(DeclarativeBase):
    __abstract__ = True
    metadata = MetaData(naming_convention=convention)

    _created_at = Column("created_at", TIMESTAMP(timezone=True), default=lambda: utcnow())
    _updated_at = Column(
        "updated_at",
        TIMESTAMP(timezone=True),
        default=lambda: utcnow(),
        onupdate=lambda: utcnow(),
    )
    _deleted_at = Column("deleted_at", TIMESTAMP(timezone=True), nullable=True)

    def __repr__(self) -> str:
        columns = ", ".join([f"{k}={repr(v)}" for k, v in self.__dict__.items() if not k.startswith("_")])
        return f"<{self.__class__.__name__}({columns})>"

    @property
    def object_type(self) -> str:
        return self.__class__.__name__

    @hybrid_property
    def created_at(self):
        return self._created_at

    @hybrid_property
    def updated_at(self):
        return self._updated_at

    @hybrid_property
    def deleted_at(self):
        return self._deleted_at

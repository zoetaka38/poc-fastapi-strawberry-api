from __future__ import annotations

import json
import logging
import uuid
from datetime import datetime, timedelta
from typing import TYPE_CHECKING, AsyncIterator, Optional

from sqlalchemy import Date, DateTime, ForeignKey, String, cast, func, or_, select
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, backref, joinedload, mapped_column, relationship, selectinload
from sqlalchemy.sql import extract
from uuid6 import uuid7

from app.datetime import utcnow

if TYPE_CHECKING:
    from .user import User

from .base import Base  # noqa: E402
from .m2m_mapping import AssigneeTaskUser  # noqa: E402

logger = logging.getLogger(__name__)


class Task(Base):
    __tablename__ = "task"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid7, index=True)
    name: Mapped[str] = mapped_column("name", String(length=255), nullable=False)
    description: Mapped[str] = mapped_column("description", String(length=255), nullable=False)
    completed_at: Mapped[datetime] = mapped_column("completed_at", DateTime(timezone=True), nullable=True)

    assignee_users: Mapped[list[User]] = relationship(
        "User",
        back_populates="assigned_tasks",
        secondary=AssigneeTaskUser.__table__,
    )

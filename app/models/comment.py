from __future__ import annotations

import logging
import uuid
from typing import TYPE_CHECKING, AsyncIterator, List, Optional

from sqlalchemy import Column, ForeignKey, String, select
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column, relationship, selectinload
from uuid6 import uuid7

if TYPE_CHECKING:
    from .tasks import Task
    from .user import User

from .base import Base  # noqa: E402

logger = logging.getLogger(__name__)


class TaskComment(Base):
    __tablename__ = "task_comment"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid7, index=True)
    text: Mapped[str] = mapped_column("text", String, nullable=True)

    task_id: Mapped[uuid.UUID] = mapped_column("task_id", UUID(as_uuid=True), ForeignKey("task.id"), nullable=False)
    task: Mapped[Task] = relationship("Task", back_populates="task_comments", foreign_keys=[task_id])

    created_by_user_id: Mapped[uuid.UUID] = mapped_column(
        "created_by_user_id", UUID(as_uuid=True), ForeignKey("user.id"), nullable=False
    )
    created_by_user: Mapped[User] = relationship(
        "User", back_populates="created_execution_step_comments", foreign_keys=[created_by_user_id]
    )

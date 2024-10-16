from __future__ import annotations

import json
import logging
import uuid
from typing import TYPE_CHECKING, AsyncIterator, Optional

from sqlalchemy import String, select
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column, relationship, selectinload
from sqlalchemy_utils import EmailType
from uuid6 import uuid7

if TYPE_CHECKING:
    from .organization import Organization
    from .tasks import Task
    from .comment import TaskComment

from .base import Base  # noqa: E402
from .m2m_mapping import AssigneeTaskUser, OrganizationUser  # noqa: E402

logger = logging.getLogger(__name__)


class User(Base):
    __tablename__ = "user"
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid7, index=True)
    name: Mapped[str] = mapped_column("name", String(length=100), nullable=False, unique=False)
    email: Mapped[str] = mapped_column("email", EmailType, unique=True, nullable=False)
    email_verified: Mapped[bool] = mapped_column("email_verified", default=False, server_default="false")
    policies: Mapped[dict[str, str]] = mapped_column("policies", JSONB, nullable=True)

    organizations: Mapped[list[Organization]] = relationship(
        "Organization",
        back_populates="users",
        secondary=OrganizationUser.__tablename__,
    )

    assigned_tasks: Mapped[list[Task]] = relationship(
        "Task",
        back_populates="assignee_users",
        secondary=AssigneeTaskUser.__tablename__,
    )

    created_task_comments: Mapped[list[TaskComment]] = relationship(
        "TaskComment",
        back_populates="created_by_user",
        foreign_keys="TaskComment.created_by_user_id",
    )

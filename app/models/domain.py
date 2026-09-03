from datetime import datetime, timezone

from sqlalchemy import DateTime, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class Organization(Base):
    __tablename__ = "organizations"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
        unique=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
        nullable=False,
    )

    assignments: Mapped[list["QuestionnaireAssignment"]] = relationship(
        back_populates="organization"
    )


class QuestionnaireTemplate(Base):
    __tablename__ = "questionnaire_templates"

    __table_args__ = (
        UniqueConstraint(
            "name",
            "version",
            name="uq_template_name_version",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    version: Mapped[int] = mapped_column(
        default=1,
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
        nullable=False,
    )

    assignments: Mapped[list["QuestionnaireAssignment"]] = relationship(
        back_populates="template"
    )


class QuestionnaireAssignment(Base):
    __tablename__ = "questionnaire_assignments"

    id: Mapped[int] = mapped_column(primary_key=True)

    organization_id: Mapped[int] = mapped_column(
        ForeignKey("organizations.id"),
        nullable=False,
    )

    template_id: Mapped[int] = mapped_column(
        ForeignKey("questionnaire_templates.id"),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="PENDING",
        nullable=False,
    )

    issued_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now,
        nullable=False,
    )

    organization: Mapped["Organization"] = relationship(back_populates="assignments")

    template: Mapped["QuestionnaireTemplate"] = relationship(
        back_populates="assignments"
    )

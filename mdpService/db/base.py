from sqlalchemy.orm import DeclarativeBase

from mdpService.db.meta import meta


class Base(DeclarativeBase):
    """Base for all models."""

    metadata = meta

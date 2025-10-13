from sqlalchemy import UUID
from sqlalchemy.orm import Mapped

from .base import Base


class User(Base):
    username: Mapped[str]
    tg_id: Mapped[int]
    id: Mapped[UUID]

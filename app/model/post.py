from uuid import UUID, uuid4

from sqlalchemy.orm import Mapped, mapped_column

from app.model.meta import Base


class Post(Base):
    __tablename__ = 'Post'

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    title: Mapped[str]
    description: Mapped[str]
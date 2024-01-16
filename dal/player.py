from sqlalchemy import Integer, VARCHAR
from sqlalchemy.orm import DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    pass


class Player(Base):
    __tablename__ = "player"

    id = mapped_column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    name = mapped_column("name", VARCHAR(100), nullable=False)
    win_count = mapped_column("win_count", Integer, nullable=False)

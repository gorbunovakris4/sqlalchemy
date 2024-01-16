from sqlalchemy import Integer, VARCHAR
from sqlalchemy.orm import DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    pass


class GameStatus(Base):
    __tablename__ = "game_status"

    id = mapped_column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    title = mapped_column("title", VARCHAR(20), nullable=False)

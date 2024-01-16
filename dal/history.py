from sqlalchemy import Integer, VARCHAR, ForeignKey, TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship
from game import Game


class Base(DeclarativeBase):
    pass


class TurnHistory(Base):
    __tablename__ = "turn_history"

    id = mapped_column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    game_id = mapped_column("game_id", Integer, ForeignKey(Game.id), nullable=False)
    game = relationship(Game, backref="game", foreign_keys=[game_id])
    turn_datetime = mapped_column(TIMESTAMP, nullable=False)
    guessed_letter = mapped_column(VARCHAR(1), nullable=False)
    current_word_status = mapped_column(VARCHAR(100), nullable=False)

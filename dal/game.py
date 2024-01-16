from sqlalchemy import Integer, VARCHAR, ForeignKey, TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship
from player import Player
from game_status import GameStatus


class Base(DeclarativeBase):
    pass


class Game(Base):
    __tablename__ = "game"

    id = mapped_column("id", Integer, primary_key=True, autoincrement=True, nullable=False)
    start_datetime = mapped_column(TIMESTAMP, nullable=False)
    end_datetime = mapped_column(TIMESTAMP, nullable=True)
    hidden_word = mapped_column("hidden_word", VARCHAR(100), nullable=False)
    player_id = mapped_column("player_id", Integer, ForeignKey(Player.id), nullable=False)
    game_status_id = mapped_column("game_status_id", Integer, ForeignKey(GameStatus.id), nullable=False)
    player = relationship(Player, backref="player", foreign_keys=[player_id])
    game_status = relationship(GameStatus, backref="game_status", foreign_keys=[game_status_id])

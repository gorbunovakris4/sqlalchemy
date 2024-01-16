import pytest
from main import TestRepository
from dal.player import Player
from dal.game import Game
from dal.game_status import GameStatus
from dal.history import TurnHistory


@pytest.fixture
def new_repository():
    return TestRepository()


def test_add(new_repository):
    new_repository.add(Player(name="player1", win_count=1))
    new_repository.add(Player(name="player2", win_count=1))


@pytest.mark.parametrize('exception', [Exception("amount cannot be negative")])
def test_bad_add(new_account, exception):
    try:
        add(new_account, -300)
    except Exception as err:
        assert err.args == exception.args
    else:
        pytest.fail("Expected error")


def test_take():
    acc = old_account(200)
    acc.take(150)
    assert acc.amount == 50


@pytest.mark.parametrize('val, exception', [(-100, Exception("amount cannot be negative")),
                                            (300, Exception("not enough money to complete the transaction"))])
def test_bad_take(val, exception):
    acc = old_account(200)
    try:
        take(acc, val)
    except Exception as err:
        assert err.args == exception.args
    else:
        pytest.fail("Expected error")


def test_history(new_account):
    add(new_account, 100)
    add(new_account, 400)
    take(new_account, 300)
    history = new_account.history
    assert history['Amount'][0] == 100
    assert history['Amount'][1] == 400
    assert history['Amount'][2] == -300
    assert history['Balance'][0] == 100
    assert history['Balance'][1] == 500
    assert history['Balance'][2] == 200

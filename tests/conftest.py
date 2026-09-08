import pytest

from services.setup import (
    init_assets_and_create_game_session,
    add_players_to_game_session,
    allocate_directors_and_nations_to_players
)


@pytest.fixture
def init_assets_and_session():
    return init_assets_and_create_game_session()

@pytest.fixture
def add_players(number: int, init_assets_and_session):
    return add_players_to_game_session(number, init_assets_and_session)

@pytest.fixture
def allocate_cards_to_players(init_assets_and_session):
    pass
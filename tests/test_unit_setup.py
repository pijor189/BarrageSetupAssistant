from unittest.mock import call, create_autospec, patch

import pytest

from exceptions.game_exceptions import NotValidNumberOfPlayersError
from models.assets import Assets
from models.director import Director
from models.nation import Nation
from models.player import Player
from models.session import Session
from services.setup import (
    add_players_to_game_session,
    allocate_directors_and_nations_to_players,
    init_assets_and_create_game_session,
)


def test_init_assets_and_create_game_session():
    assets = create_autospec(Assets)

    with (
            patch("services.data_loader.DataLoader.load_assets") as mock_load_assets,
            patch("models.session.Session.set_assets") as mock_set_assets
    ):
        mock_load_assets.return_value = assets

        session = init_assets_and_create_game_session()

        mock_load_assets.assert_called_once_with("data/assets.json")
        mock_set_assets.assert_called_once_with(assets)

    assert isinstance(session, Session)


@pytest.mark.parametrize(
    "number_of_players, name_of_players",
    [
        (1, ["John"]),
        (4, ["John", "Jack", "Thomas", "David"])
    ]
)
def test_add_players_to_game_session(number_of_players, name_of_players):
    session = create_autospec(Session)

    with (
        patch("services.setup.input", side_effect=name_of_players) as mock_input,
    ):
        players = add_players_to_game_session(number_of_players, session)

        assert mock_input.call_count == number_of_players
        mock_input.assert_called_with("Give a name of player: ")

        assert session.add_player.call_count == number_of_players
        session.add_player.assert_has_calls([
            call(player) for player in players
        ])

        assert [player.name for player in players] == name_of_players


@pytest.mark.parametrize(
    "number_of_players",
    [-1, 0, 5, "1", 1.0, [1], None]
)
def test_add_players_to_game_session_invalid(number_of_players):
    session = create_autospec(Session)

    with pytest.raises(NotValidNumberOfPlayersError):
        players = add_players_to_game_session(number_of_players, session)

        assert not players


@pytest.mark.parametrize(
    "number_of_players, special_card",
    [
        (1, False),
        (1, True),
        (2, False),
        (4, True)
    ]
)
def test_allocate_directors_and_nations_to_players(number_of_players, special_card):
    players = [create_autospec(Player) for _ in range(number_of_players)]
    if special_card and number_of_players > 1:
        players[number_of_players - 1].special_cards = []

    expected_directors = [
        create_autospec(Director)
        for _ in range(7)
    ]

    expected_nations = [
        create_autospec(Nation)
        for _ in range(4)
    ]

    for index, director in enumerate(expected_directors, start=1):
        if special_card and index == number_of_players:
            director.special_card = True
        else:
            director.special_card = False

    directors = expected_directors.copy()
    nations = expected_nations.copy()

    with (
            patch("services.data_loader.DataLoader.load_directors") as mock_load_directors,
            patch("services.data_loader.DataLoader.load_nations") as mock_load_nations,
            patch("services.setup.shuffle") as mock_shuffle
    ):
        mock_load_directors.return_value = directors
        mock_load_nations.return_value = nations

        allocate_directors_and_nations_to_players(players)

        mock_load_directors.assert_called_with("data/directors.json")
        mock_load_nations.assert_called_with("data/nations.json")
        mock_shuffle.assert_has_calls(
            [call(directors), call(nations)]
        )

        for player in players:
            assert player.director in set(expected_directors)
            assert player.nation in set(expected_nations)

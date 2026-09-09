from services.setup import (
    init_assets_and_create_game_session,
    add_players_to_game_session,
    allocate_directors_and_nations_to_players,
    ALLOWED_PLAYERS
)
from exceptions.game_exceptions import NotValidNumberOfPlayersError


try:
    print("Welcome in Barrage Setup Assistant\n\n")
    print("Create a game session and allocate assets")
    game_session = init_assets_and_create_game_session()

    print("Add players")
    number_of_players = int(input("How many players wants to play: "))
    players = add_players_to_game_session(number_of_players, game_session)

    print("Allocate directors and nations to players\n")
    allocate_directors_and_nations_to_players(players)

    print("Ready setup to play:\n")
    print(game_session)

    for player in players:
        print(player)


except NotValidNumberOfPlayersError:
    print(f"You gave not valid number of players: {number_of_players}\n"
          f"Must be in range 1-4")



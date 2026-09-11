from random import shuffle

from exceptions.game_exceptions import NotValidNumberOfPlayersError
from models.player import Player
from models.session import Session
from services.data_loader import DataLoader

ALLOWED_PLAYERS = 4


def init_assets_and_create_game_session() -> Session:
    """
        Create a game session, load assets from json file
        and set assets to session
    """
    session = Session()
    assets = DataLoader.load_assets("data/assets.json")
    session.set_assets(assets)

    return session

def add_players_to_game_session(number: int, session: Session) -> list[Player]:
    """
        Validate a number of players, read the players names
        and add them to the game session
    """
    if not isinstance(number, int) or number <= 0 or number > ALLOWED_PLAYERS:
        raise NotValidNumberOfPlayersError

    players = []
    for index in range(1, number + 1):
        name = input("Give a name of player: ")
        player = Player(name)
        players.append(player)
        session.add_player(player)

    return players

def allocate_directors_and_nations_to_players(players: list[Player]) -> None:
    """
        Load directors and nations from json file, shuffle all assets
        and allocate to players
    """
    directors = DataLoader.load_directors("data/directors.json")
    nations = DataLoader.load_nations("data/nations.json")

    if len(players) == 1:
        for director in directors.copy():
            if director.special_card:
                directors.remove(director)

    shuffle(directors)
    shuffle(nations)

    for player in players:
        player.director = directors.pop(0)
        player.nation = nations.pop(0)
        if player.director.special_card:
            player.special_cards.append(directors.pop(0))
            player.special_cards.append(directors.pop(0))

from random import shuffle

from src.barrage.assets import Assets
from src.barrage.data_loader import DataLoader
from src.barrage.director import Director
from src.barrage.nation import Nation
from src.barrage.player import Player
from src.barrage.session import Session


def init_assets_and_create_game_session() -> Session:
    session = Session()

    all_assets = DataLoader.load_assets("../../data/assets.json")

    assets = Assets(
        all_assets["turn_goals"],
        all_assets["game_goals"],
        all_assets["valleys"],
        all_assets["hills"],
        all_assets["mountains"],
        all_assets["water_drops"],
        all_assets["basic_contract"],
        all_assets["national_contract"]
    )

    session.set_assets(assets)

    return session

def add_players(number: int) -> list[Player]:
    players = []
    for index in range(1, number + 1):
        name = input("Give a name of player: ")
        players.append(Player(name))

    return players

def allocate_directors_and_nations_to_players(players: list[Player]) -> None:
    all_directors = DataLoader.load_directors("../../data/directors.json")
    all_nations = DataLoader.load_nations("../../data/nations.json")

    directors = [
        Director(
            director["name"],
            director["special_card"]
        )
        for director in all_directors
        if len(players) == 1 and not director["special_card"]
    ]
    nations = [
        Nation(
            nation["name"],
            nation["special_card"]
        )
        for nation in all_nations
    ]

    shuffle(directors)
    shuffle(nations)

    for player in players:
        player.director = directors.pop(0)
        player.nation = nations.pop(0)
        if player.director.special_card:
            player.special_cards.append(directors.pop(0))
            player.special_cards.append(directors.pop(0))

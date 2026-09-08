from random import sample

from datetime import datetime

from models.assets import Assets
from models.player import Player


class Session:
    def __init__(self):
        self.date = datetime.now().date()
        self.players = []
        self.turn_goals = []
        self.game_goals = []
        self.valleys = []
        self.hills = []
        self.mountains = []
        self.water_drops = []
        self.basic_contract = []
        self.national_contract = []


    def __repr__(self) -> str:
        return (f"Barrage session - {self.date}\n"
                f"Turn goals:\t{self.turn_goals}\n"
                f"Game goals:\t{self.game_goals}\n"
                f"Dam on valleys:\t{self.valleys}\n"
                f"Dam on hills:\t{self.hills}\n"
                f"Dam on mountains:\t{self.mountains}\n"
                f"Water drops:\t{self.water_drops}\n"
                f"Basic contract:\t{self.basic_contract}\n"
                f"National contract:\t{self.national_contract}\n"
        )


    def add_player(self, player: Player) -> None:
        self.players.append(player)


    def set_assets(self, assets: Assets) -> None:
        self.turn_goals.extend(sample(assets.turn_goals, 5))
        self.game_goals.extend(sample(assets.game_goals, 1))
        self.valleys.extend(sample(assets.valleys, 1))
        self.hills.extend(sample(assets.hills, 1))
        self.mountains.extend(sample(assets.mountains, 1))
        self.water_drops.extend(sample(assets.water_drops, 4))
        self.basic_contract.extend(sample(assets.basic_contract, 2))
        self.national_contract.extend(sample(assets.national_contract, 1))


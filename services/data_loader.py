import json

from models.assets import Assets
from models.director import Director
from models.nation import Nation


class DataLoader:
    @staticmethod
    def load_assets(path: str) -> Assets:
        with open(path, "r", encoding="utf-8") as a:
            data = json.load(a)

        return Assets(
            data["turn_goals"],
            data["game_goals"],
            data["valleys"],
            data["hills"],
            data["mountains"],
            data["water_drops"],
            data["basic_contract"],
            data["national_contract"]
        )

    @staticmethod
    def load_directors(path: str) -> list[Director]:
        with open(path, "r", encoding="utf-8") as d:
            data = json.load(d)

        return [
            Director(
                item["name"],
                item["special_card"]
            )
            for item in data
        ]


    @staticmethod
    def load_nations(path: str) -> list[Nation]:
        with open(path, "r", encoding="utf-8") as n:
            data = json.load(n)

        return [
            Nation(
                item["name"],
                item["special_card"]
            )
            for item in data
        ]

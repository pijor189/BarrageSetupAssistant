class Assets:
    def __init__(
            self,
            turn_goals,
            game_goals,
            valleys,
            hills,
            mountains,
            water_drops,
            basic_contract,
            national_contract
    ):
        self.turn_goals = turn_goals
        self.game_goals = game_goals
        self.valleys = valleys
        self.hills = hills
        self.mountains = mountains
        self.water_drops = water_drops
        self.basic_contract = basic_contract
        self.national_contract = national_contract

    def __repr__(self) -> str:
        return (f"Turn goals:\t{self.turn_goals}\n"
                f"Game goals:\t{self.game_goals}\n"
                f"Dam on valleys:\t{self.valleys}\n"
                f"Dam on hills:\t{self.hills}\n"
                f"Dam on mountains:\t{self.mountains}\n"
                f"Water drops:\t{self.water_drops}\n"
                f"Basic contract:\t{self.basic_contract}\n"
                f"National contract:\t{self.national_contract}\n"
        )

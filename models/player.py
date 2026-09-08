class Player:
    def __init__(self, name: str, director: str, nation: str):
        self.name = name
        self.director = director
        self.nation = nation
        self.special_cards = []

    def __repr__(self) -> str:
        return f"{self.name.upper()} starts with {self.director} and {self.nation}\n\
                {self.special_cards if self.special_cards else ""}"

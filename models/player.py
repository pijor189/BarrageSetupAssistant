class Player:
    def __init__(self, name: str):
        self.name = name
        self.director = None
        self.nation = None
        self.special_cards = []

    def __repr__(self) -> str:
        return f"{self.name.upper()} starts with {self.director} and {self.nation}\n\
                {self.special_cards if self.special_cards else ""}"

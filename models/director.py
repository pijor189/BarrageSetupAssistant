class Director:
    def __init__(self, name, special_card):
        self.name = name
        self.special_card = special_card

    def __repr__(self) -> str:
        return f"Director {self.name}"

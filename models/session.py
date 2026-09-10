from random import sample
from datetime import datetime
from rich.table import Table
from rich.console import Console

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


    @staticmethod
    def _format_list(items: list) -> str:
        return ", ".join(str(item) for item in items) if items else "-"


    def __repr__(self) -> str:
        """Create a formatted table with Rich library"""
        console = Console()

        # Create table
        table = Table(
            title=f"🎮 BARRAGE SESSION - {self.date}",
            show_header=True,
            header_style="bold magenta"
        )
        table.add_column("Asset Type", style="cyan", width=25)
        table.add_column("Values", style="green")

        # Add rows
        table.add_row("Turn goals", self._format_list(self.turn_goals))
        table.add_row("Game goals", self._format_list(self.game_goals))
        table.add_row("Dam on valleys", self._format_list(self.valleys))
        table.add_row("Dam on hills", self._format_list(self.hills))
        table.add_row("Dam on mountains", self._format_list(self.mountains))
        table.add_row("Water drops", self._format_list(self.water_drops))
        table.add_row("Basic contract", self._format_list(self.basic_contract))
        table.add_row("National contract", self._format_list(self.national_contract))

        # Render to string
        with console.capture() as capture:
            console.print(table)

        return capture.get()


    def add_player(self, player: Player) -> None:
        """Add player to game session"""
        self.players.append(player)


    def set_assets(self, assets: Assets) -> None:
        """Set assets to game session"""
        self.turn_goals.extend(sample(assets.turn_goals, 5))
        self.game_goals.extend(sample(assets.game_goals, 1))
        self.valleys.extend(sample(assets.valleys, 1))
        self.hills.extend(sample(assets.hills, 1))
        self.mountains.extend(sample(assets.mountains, 1))
        self.water_drops.extend(sample(assets.water_drops, 4))
        self.basic_contract.extend(sample(assets.basic_contract, 2))
        self.national_contract.extend(sample(assets.national_contract, 1))

from rich.console import Console
from rich.panel import Panel
from rich.text import Text


class Player:
    def __init__(self, name: str):
        self.name = name
        self.director = None
        self.nation = None
        self.special_cards = []

    def __repr__(self) -> str:
        """Create a formatted player info with Rich library"""
        console = Console()

        # Create player name with emphasis
        player_name = Text(f"🎯 {self.name.upper()} 🎯", style="bold bright_yellow", justify="center")

        # Build content
        content = player_name + "\n\n"
        content += f"👨‍💼 Director:  {self.director}\n"
        content += f"🌍 Nation:  {self.nation}\n"

        # Add special cards if they exist
        if self.special_cards:
            content += "\n⭐ Special Cards:\n"
            for card in self.special_cards:
                content += f"  • {card}\n"

        # Create panel
        panel = Panel(
            content,
            border_style="green",
            expand=False,
            padding=(1, 2)
        )

        # Render to string
        with console.capture() as capture:
            console.print(panel)

        return capture.get()

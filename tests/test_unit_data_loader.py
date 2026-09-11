from unittest.mock import MagicMock, patch

from models.assets import Assets
from models.director import Director
from models.nation import Nation
from services.data_loader import DataLoader


def test_load_assets():
    path = "test_path"
    file_payload = MagicMock()
    json_payload = {
        "turn_goals": [],
        "game_goals": [],
        "valleys": [],
        "hills": [],
        "mountains": [],
        "water_drops": [],
        "basic_contract": [],
        "national_contract": []
    }

    with (
        patch("services.data_loader.open", return_value=file_payload) as mock_open,
        patch("services.data_loader.json.load", return_value=json_payload) as mock_load
    ):
        result = DataLoader.load_assets(path)

        file_payload.__enter__.assert_called_once()
        file_payload.__exit__.assert_called_once()
        mock_open.assert_called_once_with(path, "r", encoding="utf-8")
        mock_load.assert_called_once_with(file_payload.__enter__.return_value)
        assert isinstance(result, Assets)


def test_load_directors():
    path = "test_path"
    file_payload = MagicMock()
    json_payload = [
        {
            "name": "John",
            "special_card": True
        },
        {
            "name": "Jack",
            "special_card": False
        },
        {
            "name": "Adam",
            "special_card": False
        }
    ]

    with (
        patch("services.data_loader.open", return_value=file_payload) as mock_open,
        patch("services.data_loader.json.load", return_value=json_payload) as mock_load
    ):
        result = DataLoader.load_directors(path)

        file_payload.__enter__.assert_called_once()
        file_payload.__exit__.assert_called_once()
        mock_open.assert_called_once_with(path, "r", encoding="utf-8")
        mock_load.assert_called_once_with(file_payload.__enter__.return_value)

        assert isinstance(result, list)
        for index in range(len(result)):
            assert isinstance(result[index], Director)
            assert result[index].name == json_payload[index]["name"]
            assert result[index].special_card == json_payload[index]["special_card"]


def test_load_nations():
    path = "test_path"
    file_payload = MagicMock()
    json_payload = [
        {
            "name": "America",
            "special_card": True
        },
        {
            "name": "Italy",
            "special_card": False
        },
        {
            "name": "Poland",
            "special_card": False
        }
    ]

    with (
        patch("services.data_loader.open", return_value=file_payload) as mock_open,
        patch("services.data_loader.json.load", return_value=json_payload) as mock_load
    ):
        result = DataLoader.load_nations(path)

        file_payload.__enter__.assert_called_once()
        file_payload.__exit__.assert_called_once()
        mock_open.assert_called_once_with(path, "r", encoding="utf-8")
        mock_load.assert_called_once_with(file_payload.__enter__.return_value)

        assert isinstance(result, list)
        for index in range(len(result)):
            assert isinstance(result[index], Nation)
            assert result[index].name == json_payload[index]["name"]
            assert result[index].special_card == json_payload[index]["special_card"]

from unittest.mock import MagicMock

class user_data:
    def get_user_data(self):
        # Holt Benutzerdaten via API
        pass

# Test-Klasse

class TestUser:
    def api_returns_data(self):

        api_content = user_data()
        api_content.get_user_data = MagicMock(
            return_value={"Username": "Johnny", "Office": "Grenchen"})

        # Rufe die Methode auf
        result = api_content.get_user_data("Johnny")

        # Überprüfen, ob die Methode aufgerufen wurde
        api_content.get_user_data.assert_called_once_with("Johnny")
        assert result == {"Username": "Johnny", "Office": "Grenchen"}


TestUser().api_returns_data()
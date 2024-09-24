from unittest.mock import MagicMock

class User:
    def has_admin_rights(self):
        # Überprüft, ob der Benutzer Adminrechte hat
        pass

# Test-Klasse
class TestUser:
    def test_has_admin_rights(self):

        user = User()
        user.has_admin_rights = MagicMock(return_value=True)

        # Rufe die Methode auf
        result = user.has_admin_rights()

        # Überprüfen, ob die Methode aufgerufen wurde
        user.has_admin_rights.assert_called_once()
        assert result == True

TestUser().test_has_admin_rights()
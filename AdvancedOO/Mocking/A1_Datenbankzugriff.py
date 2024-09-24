from unittest.mock import MagicMock


class DatabaseHandler:
    def save_record(self, data):
        # Speichert Daten in der Datenbank
        pass

# Test-Klasse


class TestDatabaseHandler:
    def test_save_record(self):
        db_handler = DatabaseHandler()
        db_handler.save_record = MagicMock(return_value=True)

        # Rufe die Methode mit Testdaten auf
        result = db_handler.save_record({"name": "Test User", "age": 30})

        # Überprüfen, ob die Methode aufgerufen wurde
        db_handler.save_record.assert_called_once_with({"name": "Test User", "age": 30})
        assert result == True

TestDatabaseHandler().test_save_record()

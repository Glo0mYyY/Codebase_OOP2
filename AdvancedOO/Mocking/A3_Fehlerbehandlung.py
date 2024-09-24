from unittest.mock import MagicMock

class FileLoader:
    def load_file(self, file_name):
        # Läd eine Datei
        pass
    # Test-Klasse

class TestFileLoader:
    def test_load_file_exception(self):
        file_loader = FileLoader()
        file_loader.load_file = MagicMock(
            side_effect=FileNotFoundError("File not found"))
        # Fangen der Ausnahme
        try:
            file_loader.load_file("non_existing_file.txt")
        except FileNotFoundError as e:
            assert str(e) == "File not found"

TestFileLoader().test_load_file_exception()
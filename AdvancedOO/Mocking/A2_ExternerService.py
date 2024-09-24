from unittest.mock import MagicMock


class WeatherService:

    def get_weather(self, location):

        # Holt Wetterdaten von einem externen Service
        pass

    # Test-Klasse


class TestWeatherService:
    def test_get_weather(self):

        weather_service = WeatherService()
        weather_service.get_weather = MagicMock(
            return_value={"temp": 22, "condition": "sunny"})

        # Rufe die Methode mit einem Test-Ort auf
        result = weather_service.get_weather("Berlin")

        # Überprüfen, ob die Methode aufgerufen wurde
        weather_service.get_weather.assert_called_once_with("Berlin")
        assert result == {"temp": 22, "condition": "sunny"}


TestWeatherService().test_get_weather()

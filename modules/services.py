import requests

class ApiService:
    __API_KEY = "e21fa6b6f1844d30a1f20703251009"
    __URL = "http://api.weatherapi.com/v1"

    def get_weather_data(self, query, forecast_days=1, lang="pt"):
        endpoint = "/forecast.json"
        params = {
            "key": self.__API_KEY,
            "q": query,
            "days": forecast_days,
            "alerts": "yes",
            "lang": lang
        }
        return self.__make_request(endpoint, params)

    def get_historical_data(self, query, date, lang="pt"):
        endpoint = "/history.json"
        params = {
            "key": self.__API_KEY,
            "q": query,
            "dt": date,
            "lang": lang
        }
        return self.__make_request(endpoint, params)

    def __make_request(self, endpoint, params):
        try:
            url_completa = f"{self.__URL}{endpoint}"
            response = requests.get(url_completa, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição à WeatherAPI.com: {e}")
            return None
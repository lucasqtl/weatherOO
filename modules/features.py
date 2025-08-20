from .models import ForecastDay

class Feature:
    def __init__(self, api_service, ui_manager):
        self.api = api_service
        self.ui = ui_manager

    def execute(self):
        pass

class Forecast(Feature):

    def execute(self): 
        while True:
            try:
                city = self.ui.get_user_input('enter_city')
                period = self.ui.get_user_input('enter_period')

                if period not in ['1', '3', '7']:
                    self.ui.display_message('invalid_period')
                    continue

                language = self.ui.get_language()
                weather_data = self.api.get_weather_data(city, period, language)

                if weather_data:
                    forecast_objects = [ForecastDay.from_dict(day_data) for day_data in weather_data['forecast']['forecastday']]
                    
                    self.ui.display_forecast(city, forecast_objects)

                option = self.ui.get_user_input('consult_another_city')
                if option.lower() != 'c':
                    break

            except Exception as e:
                self.ui.display_message('invalid_input')
                print(f"Erro inesperado: {e}")
                break
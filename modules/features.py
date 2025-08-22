from .models import ForecastDay, CurrentWeather

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

class Current(Feature): 

    def execute(self):
        while True:
            try:
                print('\n' + '='*30)
                self.ui.display_message('my_location')
                self.ui.display_message('another_location')
                print('='*30)
                option = self.ui.get_user_input('choose_option')

                if option == '1':
                    query = "auto:ip"
                elif option == '2':
                    query = self.ui.get_user_input('enter_city')
                else:
                    self.ui.display_message('invalid_input')
                    continue

                language = self.ui.get_language()
                weather_data_dict = self.api.get_weather_data(query, 1, language)

                if weather_data_dict:
                    current_weather_obj = CurrentWeather.from_dict(weather_data_dict)
                    
                    self.ui.display_current_weather(current_weather_obj)

                # Usando uma chave de tradução mais genérica para o submenu
                another = self.ui.get_user_input('consult_another_city')
                if another.lower() != 'c':
                    break

            except Exception as e:
                self.ui.display_message('invalid_input')
                print(f"Erro inesperado: {e}")
                break

class History(Feature):

    def execute(self):
        while True:
            try:
                print('\n' + '='*30)
                city = self.ui.get_user_input('enter_city')
                self.ui.display_message('historical_note')
                date = self.ui.get_user_input('enter_date')
                print('='*30)

                language = self.ui.get_language()
                historical_data = self.api.get_historical_data(city, date, language)

                if historical_data:
                    historical_obj = CurrentWeather.from_dict(historical_data)
                    
                    self.ui.display_historical_weather(historical_obj)

                # Usando uma chave de tradução mais genérica para o submenu
                another = self.ui.get_user_input('consult_another_city')
                if another.lower() != 'c':
                    break

            except Exception as e:
                self.ui.display_message('invalid_input')
                print(f"Erro inesperado: {e}")
                break
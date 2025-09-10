from .models import ForecastDay, CurrentWeather, HistoricalDay, AlertWeather, WeatherReport
from .models import Feedback as FeedbackModel
from datetime import datetime, timedelta
from abc import ABC, abstractmethod

MAX_DAYS_FOR_REPORT = 30 

class Feature(ABC):
    def __init__(self, api_service, ui_manager):
        self.api = api_service
        self.ui = ui_manager

    @abstractmethod
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
                self.ui.display_message('unexpected_error', error=str(e))
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

                another = self.ui.get_user_input('consult_another_city')
                if another.lower() != 'c':
                    break

            except Exception as e:
                self.ui.display_message('invalid_input')
                self.ui.display_message('unexpected_error', error=str(e))
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
                    historical_obj = HistoricalDay.from_dict(historical_data)
                    
                    self.ui.display_historical_weather(city, historical_obj)

                another = self.ui.get_user_input('consult_another_city')
                if another.lower() != 'c':
                    break

            except Exception as e:
                self.ui.display_message('invalid_input')
                self.ui.display_message('unexpected_error', error=str(e))
                break

class Feedback(Feature):
    def __init__(self, api_service, ui_manager, feedbacks_list):
        super().__init__(api_service, ui_manager)
        self.feedbacks = feedbacks_list

    def execute(self):
        while True:
            self.ui.display_message('feedback_menu')
            option = self.ui.get_user_input('feedback_choice')

            if option == '1':
                self._add_feedback()
                another = self.ui.get_user_input('feedback_another')
                if another.lower() != 'f':
                    break
            
            elif option == '2':
                self.ui.display_feedbacks(self.feedbacks)
                self.ui.get_user_input('press_enter_to_continue')
                break

            else:
                self.ui.display_message('invalid_input')
                break

    def _add_feedback(self):
        location = self.ui.get_user_input('enter_location')
        condition = self.ui.get_user_input('enter_condition')
        date = self.ui.get_user_input('enter_feedback_date')
        comment = self.ui.get_user_input('enter_comment')
        
        new_feedback = FeedbackModel(condition, location, date, comment)
        self.feedbacks.append(new_feedback)
        self.ui.display_message('sucess_feedback')

MAX_DAYS_FOR_REPORT = 30 

class Alert(Feature):
    def execute(self):
        while True:
            try:
                city = self.ui.get_user_input('enter_alert_city')
                language = self.ui.get_language()
                weather_data = self.api.get_weather_data(city, 7, language)

                if weather_data and 'alerts' in weather_data and weather_data['alerts']['alert']:
                    alerts_list = weather_data['alerts']['alert']
                    alert_objects = [AlertWeather.from_dict(alert_dict) for alert_dict in alerts_list]
                    self.ui.display_alerts(city, alert_objects)

                else:
                    self.ui.display_message('no_alerts')

                self.ui.get_user_input('press_enter_to_continue') # Apenas para pausar
                break

            except Exception as e:
                self.ui.display_message('invalid_input')
                break

class Report(Feature):
    def execute(self):
        try:
            city = self.ui.get_user_input('report_city_prompt')
            self.ui.display_message('report_dates_prompt')
            self.ui.display_message('report_date_format_prompt')
            date1_str = self.ui.get_user_input('report_date1_prompt')
            date2_str = self.ui.get_user_input('report_date2_prompt')

            date1_obj = datetime.strptime(date1_str, '%Y-%m-%d').date()
            date2_obj = datetime.strptime(date2_str, '%Y-%m-%d').date()

            if date1_obj > date2_obj:
                self.ui.display_message('report_date_error_order')
                return

            num_days = (date2_obj - date1_obj).days + 1 
            if num_days > MAX_DAYS_FOR_REPORT:
                self.ui.display_message('report_date_error_limit')
                return

            current_date = date1_obj

            max_temp_period = float('-inf')
            min_temp_period = float('inf') 
            total_precip = num_rainy_days = total_avg_temp = total_avg_umidity = num_days_with_data = 0

            print("\nColetando e analisando dados...")
            while current_date <= date2_obj:
                date_str = current_date.isoformat()
                historical_data = self.api.get_historical_data(city, date_str, self.ui.get_language())

                if historical_data:
                    historical_obj = HistoricalDay.from_dict(historical_data)

                    if historical_obj.max_temp > max_temp_period:
                        max_temp_period = historical_obj.max_temp
                    if historical_obj.min_temp < min_temp_period:
                        min_temp_period = historical_obj.min_temp

                    total_precip += historical_obj.total_precip
                    total_avg_temp += historical_obj.avg_temp
                    total_avg_umidity += historical_obj.avg_humidity
                    
                    if historical_obj.total_precip > 0:
                        num_rainy_days += 1
                    
                    num_days_with_data += 1
                
                current_date += timedelta(days=1)
            
            if num_days_with_data > 0:
                final_avg_temp = total_avg_temp / num_days_with_data
                final_avg_humidity = total_avg_umidity / num_days_with_data

                report_obj = WeatherReport(
                    city, date1_str, date2_str, max_temp_period, min_temp_period,
                    total_precip, num_rainy_days, final_avg_temp, final_avg_humidity
                )
                
                self.ui.display_report(report_obj)
            else:
                self.ui.display_message('report_no_data')
                    
        except ValueError:
            self.ui.display_message('report_invalid_date_format')
            return
        except Exception:
            self.ui.display_message('invalid_input')
            return

        
        
        
        
        
        
        
   
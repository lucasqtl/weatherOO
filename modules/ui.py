from .models import CurrentWeather, HistoricalDay, WeatherReport

class UIManager:
    __translations = {
    'pt': {
        'select_feature': 'Selecione uma funcionalidade:',
        'weather_forecast': '1 - Previsão do Tempo:',
        'current_weather_data': '2 - Dados do clima atual:',
        'historical_data': '3 - Dados Históricos:',
        'report_local_weather': '4 - Reportar clima local:',
        'climate_analysis': '5 - Análise do Clima:',
        'severe_weather_alerts': '6 - Alertas de Clima Severo:',
        'select_language': '7 - Selecionar Idioma:',
        'close_menu': '0 - Fechar Menu:',
        'choose_option': 'Qual opção deseja? ',
        'enter_city': 'Digite a sua cidade: ',
        'enter_period': 'Digite o período de previsão (1, 3 ou 7 dias): ',
        'invalid_period': 'Período inválido. Por favor, escolha entre 1, 3 ou 7 dias.',
        'text_city': 'Previsão para os próximos {period} dias em {city}',
        'day': 'Dia',
        'max_temp': 'Temperatura máxima',
        'min_temp': 'Temperatura mínima',
        'conditions': 'Condições',
        'sunrise': 'Nascer do Sol',
        'sunset': 'Pôr do Sol',
        'temperature': 'Temperatura',
        'my_location': '1 - Consultar clima da localização atual',
        'another_location': '2 - Consultar clima de uma cidade específica',
        'consult_another_city': 'Digite "c" para consultar outra cidade ou "m" para voltar ao menu: ',
        'invalid_input': 'Entrada inválida, retornando ao menu',
        'weather_in_city': 'Como está o tempo em {city}',
        'humidity': 'Umidade',
        'wind_speed': 'Velocidade do vento',
        'precipitation': 'Precipitação',
        'enter_alert_city': 'Digite a cidade que você quer consultar se há alertas: ',
        'weather_alerts': 'Temos alertas climáticos nos próximos 7 dias em',
        'alert_title': 'Título',
        'alert_description': 'Descrição',
        'alert_severity': 'Severidade',
        'alert_urgency': 'Urgência',
        'alert_areas': 'Áreas afetadas',
        'no_alerts': 'Não existem alertas climáticos para a sua cidade nos próximos 7 dias.',
        'historical_note': 'OBS: Temos dados históricos de até 1 ano atrás',
        'enter_date': 'Digite a data que você quer consultar (formato: yyyy-MM-dd): ',
        'historical_weather': 'Como estava o tempo no dia {date} em {city}',
        'total_precip': 'Precipitação Total',
        'max_wind_speed': 'Velocidade Máxima do Vento',
        'avg_humidity': 'Umidade média',
        'feedback_menu': '1 - Enviar um Feedback\n2 - Visualizar feedbacks enviados',
        'feedback_choice': 'O que Deseja? ',
        'enter_location': 'Insira a sua localização: ',
        'enter_condition': 'Insira a condição do tempo: ',
        'enter_feedback_date': 'Insira a data (formato: yyyy-MM-dd): ',
        'enter_comment': 'Insira o seu comentário: ',
        'feedback_another': 'Deseja enviar outro feedback ou ver os feedbacks enviados? Digite "f" ou digite "m" para voltar ao menu: ',
        'no_feedbacks': 'Não há feedbacks registrados',
        'feedback_number': 'Feedback',
        'report_city_prompt': 'Qual cidade deseja consultar? ',
        'report_dates_prompt': 'Escolha duas datas com intervalo máximo de 30 dias e será feita uma análise: ',
        'report_date_format_prompt': 'Se atente ao formato: yyyy-MM-dd',
        'report_date1_prompt': 'Digite a primeira data: ',
        'report_date2_prompt': 'Digite a segunda data: ',
        'report_date_error_order': 'A data de início deve ser anterior ou igual à data de fim.',
        'report_date_error_limit': 'O intervalo de datas é muito grande. O limite é de {MAX_DAYS_FOR_REPORT} dias.',
        'report_title': 'Relatório de {city} de {date1} a {date2}',
        'report_max_temp': 'Maior temperatura no período: {max_temp_period}°',
        'report_min_temp': 'Menor temperatura no período: {min_temp_period}°',
        'report_total_precip': 'Total de precipitação no período: {total_precip:.2f}mm',
        'report_rainy_days': 'Número de dias chuvosos: {num_rainy_days}',
        'report_avg_temp': 'Média de temperatura no período: {final_avg_temp:.2f}°',
        'report_avg_umidity': 'Média de umidade no período: {final_avg_humidity:.2f}%',
        'report_no_data': 'Não foi possível obter dados para o período e cidade informados.',
        'report_invalid_date_format': 'Formato de data inválido. Use yyyy-MM-dd.',
        'press_enter_to_continue': '\nPressione Enter para voltar ao menu...',
        'sucess_feedback': 'Feedback adicionado com sucesso!',
        'unexpected_error': 'Erro inesperado: {error}',
    },
    'en': {
        'select_feature': 'Select a feature:',
        'weather_forecast': '1 - Weather Forecast:',
        'current_weather_data': '2 - Current Weather Data:',
        'historical_data': '3 - Historical Data:',
        'report_local_weather': '4 - Report Local Weather:',
        'climate_analysis': '5 - Climate Analysis:',
        'severe_weather_alerts': '6 - Severe Weather Alerts:',
        'select_language': '7 - Select Language:',
        'close_menu': '0 - Close Menu:',
        'choose_option': 'Which option do you want? ',
        'enter_city': 'Enter your city: ',
        'enter_period': 'Enter the forecast period (1, 3, or 7 days): ',
        'invalid_period': 'Invalid period. Please choose between 1, 3, or 7 days.',
        'text_city': 'Forecast for the next {period} days in {city}',
        'day': 'Day',
        'max_temp': 'Maximum Temperature',
        'min_temp': 'Minimum Temperature',
        'conditions': 'Conditions',
        'sunrise': 'Sunrise',
        'sunset': 'Sunset',
        'temperature': 'Temperature',
        'my_location': '1 - Check weather for current location',
        'another_location': '2 - Check weather for a specific city',
        'consult_another_city': 'Type "c" to consult another city or "m" to return to the menu: ',
        'invalid_input': 'Invalid input, returning to menu',
        'weather_in_city': 'How is the weather in {city}',
        'humidity': 'Humidity',
        'wind_speed': 'Wind Speed',
        'precipitation': 'Precipitation',
        'enter_alert_city': 'Enter the city you want to check for alerts: ',
        'weather_alerts': 'We have weather alerts for the next 7 days in',
        'alert_title': 'Title',
        'alert_description': 'Description',
        'alert_severity': 'Severity',
        'alert_urgency': 'Urgency',
        'alert_areas': 'Affected Areas',
        'no_alerts': 'There are no weather alerts for your city in the next 7 days.',
        'historical_note': 'Note: We have historical data from up to 1 year ago',
        'enter_date': 'Enter the date you want to check (format: yyyy-MM-dd): ',
        'historical_weather': 'How was the weather on {date} in {city}',
        'total_precip': 'Total Precipitation',
        'max_wind_speed': 'Maximum Wind Speed',
        'avg_humidity': 'Average Humidity',
        'feedback_menu': '1 - Send a Feedback\n2 - View sent feedbacks',
        'feedback_choice': 'What do you want? ',
        'enter_location': 'Enter your location: ',
        'enter_condition': 'Enter the weather condition: ',
        'enter_feedback_date': 'Enter the date (format: yyyy-MM-dd): ',
        'enter_comment': 'Enter your comment: ',
        'feedback_another': 'Do you want to send another feedback or view sent feedbacks? Type "f" or type "m" to return to the menu: ',
        'no_feedbacks': 'No feedbacks registered',
        'feedback_number': 'Feedback',
        'report_city_prompt': 'Which city would you like to consult? ',
        'report_dates_prompt': 'Choose two dates with a maximum interval of 30 days for analysis: ',
        'report_date_format_prompt': 'Pay attention to the format: yyyy-MM-dd',
        'report_date1_prompt': 'Enter the first date: ',
        'report_date2_prompt': 'Enter the second date: ',
        'report_date_error_order': 'The start date must be earlier than or equal to the end date.',
        'report_date_error_limit': 'The date range is too large. The limit is {MAX_DAYS_FOR_REPORT} days.',
        'report_title': 'Report of {city} from {date1} to {date2}',
        'report_max_temp': 'Highest temperature in the period: {max_temp_period}°',
        'report_min_temp': 'Lowest temperature in the period: {min_temp_period}°',
        'report_total_precip': 'Total precipitation in the period: {total_precip:.2f}mm',
        'report_rainy_days': 'Number of rainy days: {num_rainy_days}',
        'report_avg_temp': 'Average temperature in the period: {final_avg_temp:.2f}°',
        'report_avg_umidity': 'Average humidity in the period: {final_avg_humidity:.2f}%',
        'report_no_data': 'Could not retrieve data for the specified period and city.',
        'report_invalid_date_format': 'Invalid date format. Use yyyy-MM-dd.',
        'press_enter_to_continue': '\nPress Enter to return to the menu...',
        'sucess_feedback': 'Feedback added successfully!',
        'unexpected_error': 'Unexpected error: {error}',
    },
    'es': {
        'select_feature': 'Seleccione una funcionalidad:',
        'weather_forecast': '1 - Pronóstico del Tiempo:',
        'current_weather_data': '2 - Datos del clima actual:',
        'historical_data': '3 - Datos Históricos:',
        'report_local_weather': '4 - Reportar Clima Local:',
        'climate_analysis': '5 - Análisis Climático:',
        'severe_weather_alerts': '6 - Alertas de Clima Severo:',
        'select_language': '7 - Seleccionar Idioma:',
        'close_menu': '0 - Cerrar Menú:',
        'choose_option': '¿Qué opción desea? ',
        'enter_city': 'Ingrese su ciudad: ',
        'enter_period': 'Ingrese el período de pronóstico (1, 3 o 7 días): ',
        'invalid_period': 'Período inválido. Por favor, elija entre 1, 3 o 7 días.',
        'text_city': 'Pronóstico para los próximos {period} días en {city}',
        'day': 'Día',
        'max_temp': 'Temperatura máxima',
        'min_temp': 'Temperatura mínima',
        'conditions': 'Condiciones',
        'sunrise': 'Amanecer',
        'sunset': 'Atardecer',
        'temperature': 'Temperatura',
        'my_location': '1 - Consultar clima de la ubicación actual',
        'another_location': '2 - Consultar clima de una ciudad específica',
        'consult_another_city': 'Escriba "c" para consultar otra ciudad o "m" para volver al menú: ',
        'invalid_input': 'Entrada inválida, regresando al menú',
        'weather_in_city': 'Cómo está el tiempo en {city}',
        'humidity': 'Humedad',
        'wind_speed': 'Velocidad del viento',
        'precipitation': 'Precipitación',
        'enter_alert_city': 'Ingrese la ciudad que desea consultar si hay alertas: ',
        'weather_alerts': 'Tenemos alertas climáticas para los próximos 7 días en',
        'alert_title': 'Título',
        'alert_description': 'Descripción',
        'alert_severity': 'Severidad',
        'alert_urgency': 'Urgencia',
        'alert_areas': 'Áreas afectadas',
        'no_alerts': 'No hay alertas climáticas para su ciudad en los próximos 7 días.',
        'historical_note': 'Nota: Tenemos datos históricos de hasta 1 año atrás',
        'enter_date': 'Ingrese la fecha que desea consultar (formato: yyyy-MM-dd): ',
        'historical_weather': 'Cómo estaba el tiempo el {date} en {city}',
        'total_precip': 'Precipitación Total',
        'max_wind_speed': 'Velocidad Máxima del Viento',
        'avg_humidity': 'Humedad promedio',
        'feedback_menu': '1 - Enviar un Feedback\n2 - Ver feedbacks enviados',
        'feedback_choice': '¿Qué desea? ',
        'enter_location': 'Ingrese su ubicación: ',
        'enter_condition': 'Ingrese la condición del tiempo: ',
        'enter_feedback_date': 'Ingrese la fecha (formato: yyyy-MM-dd): ',
        'enter_comment': 'Ingrese su comentario: ',
        'feedback_another': 'Desea enviar otro feedback o ver los feedbacks enviados? Escriba "f" o escriba "m" para volver al menú: ',
        'no_feedbacks': 'No hay feedbacks registrados',
        'feedback_number': 'Feedback',
        'report_city_prompt': '¿Qué ciudad desea consultar? ',
        'report_dates_prompt': 'Elija dos fechas con un intervalo máximo de 30 días para un análisis: ',
        'report_date_format_prompt': 'Preste atención al formato: yyyy-MM-dd',
        'report_date1_prompt': 'Ingrese la primera fecha: ',
        'report_date2_prompt': 'Ingrese la segunda fecha: ',
        'report_date_error_order': 'La fecha de inicio debe ser anterior o igual a la fecha de fin.',
        'report_date_error_limit': 'El intervalo de fechas es demasiado grande. El límite es de {MAX_DAYS_FOR_REPORT} días.',
        'report_title': 'Informe de {city} desde {date1} hasta {date2}',
        'report_max_temp': 'Temperatura más alta en el período: {max_temp_period}°',
        'report_min_temp': 'Temperatura más baja en el período: {min_temp_period}°',
        'report_total_precip': 'Precipitación total en el período: {total_precip:.2f}mm',
        'report_rainy_days': 'Número de días lluviosos: {num_rainy_days}',
        'report_avg_temp': 'Temperatura promedio en el período: {final_avg_temp:.2f}°',
        'report_avg_umidity': 'Humedad promedio en el período: {final_avg_humidity:.2f}%',
        'report_no_data': 'No se pudieron obtener datos para el período y ciudad especificados.',
        'report_invalid_date_format': 'Formato de fecha inválido. Use yyyy-MM-dd.',
        'press_enter_to_continue': '\nPresione Enter para volver al menú...',
        'sucess_feedback': '¡Feedback agregado con éxito!',
        'unexpected_error': 'Error inesperado: {error}'
    }
}

    def __init__(self, language='pt'):
        if language not in self.__translations:
            print(f"Idioma '{language}' não suportado. Usando Português (pt) por padrão.")
            self._language = 'pt'
        else:
            self._language = language

    def set_language(self, language):
        if language in self.__translations:
            self._language = language
            return True 
        print(f"Idioma '{language}' não suportado.")
        return False

    def display_main_menu(self):
        print('\n' + '='*30)
        print(self.__translations[self._language]['select_feature'])
        print(self.__translations[self._language]['weather_forecast'])
        print(self.__translations[self._language]['current_weather_data'])
        print(self.__translations[self._language]['historical_data'])
        print(self.__translations[self._language]['report_local_weather'])
        print(self.__translations[self._language]['climate_analysis'])
        print(self.__translations[self._language]['severe_weather_alerts'])
        print(self.__translations[self._language]['select_language'])
        print(self.__translations[self._language]['close_menu'])
        print('='*30)

    def get_language(self):
        return self._language

    def get_text(self, key, **kwargs):
        text_template = self.__translations[self._language].get(key, f"Chave '{key}' não encontrada.")
        try:
            return text_template.format(**kwargs)
        except KeyError as e:
            return f"Erro de formatação: placeholder {e} faltando nos argumentos."

    def get_user_input(self, prompt_key, **kwargs):
        prompt_text = self.get_text(prompt_key, **kwargs)
        return input(prompt_text)

    def display_message(self, message_key, **kwargs):
        message_text = self.get_text(message_key, **kwargs)
        print(message_text)

    def display_forecast(self, city_name, forecast_days):
        self.display_message('text_city', period=len(forecast_days), city=city_name.title())

        for i, day in enumerate(forecast_days, 1):
            print('\n' + '='*30)
            print(f"{self.get_text('day')} {i}:")
            print(f"{self.get_text('day')}: {day.date}")
            print(f"{self.get_text('max_temp')}: {day.max_temp_c}°")
            print(f"{self.get_text('min_temp')}: {day.min_temp_c}°")
            print(f"{self.get_text('conditions')}: {day.condition}")
            print(f"{self.get_text('sunrise')}: {day.sunrise}")
            print(f"{self.get_text('sunset')}: {day.sunset}")
            print('='*30)

    def display_current_weather(self, weather: CurrentWeather):
        print('\n' + '='*30)
        self.display_message('weather_in_city', city=weather.city.title())
        print(f"{self.get_text('temperature')}: {weather.temp_c}°")
        print(f"{self.get_text('conditions')}: {weather.condition}")
        print(f"{self.get_text('humidity')}: {weather.humidity}%")
        print(f"{self.get_text('wind_speed')}: {weather.wind_kph}km/h")
        print(f"{self.get_text('precipitation')}: {weather.precip_mm}mm")
        print('='*30)

    def display_historical_weather(self, city_name, weather: HistoricalDay):
        print('\n' + '='*30)
        self.display_message('historical_weather', date=weather.date, city=city_name.title())
        print(f"{self.get_text('max_temp')}: {weather.max_temp}°")
        print(f"{self.get_text('min_temp')}: {weather.min_temp}°")
        print(f"{self.get_text('conditions')}: {weather.condition}")
        print(f"{self.get_text('total_precip')}: {weather.total_precip}mm")
        print(f"{self.get_text('max_wind_speed')}: {weather.max_wind_speed}km/h")
        print(f"{self.get_text('avg_humidity')}: {weather.avg_humidity}%")
        print(f"{self.get_text('sunrise')}: {weather.sunrise}")
        print(f"{self.get_text('sunset')}: {weather.sunset}")
        print('='*30)

    def display_feedbacks(self, feedbacks_list):
        if not feedbacks_list:
            self.display_message('no_feedbacks')
            return

        print('\n' + '='*30)
        self.display_message('feedback_number')
        for i, feedback in enumerate(feedbacks_list, 1):
            print(f"--- Feedback #{i} ---{feedback}")
        print('='*30)

    def display_alerts(self, city_name, alert_items):
        self.display_message('weather_alerts', city=city_name.title())

        for i, day in enumerate(alert_items, 1):
            print('\n' + '='*30)
            print(f"{self.get_text('day')} {i}:")
            print(f"{self.get_text('alert_title')}: {day.headline}")
            print(f"{self.get_text('alert_description')}: {day.desc}")
            print(f"{self.get_text('alert_severity')}: {day.severity}")
            print(f"{self.get_text('alert_urgency')}: {day.urgency}")
            print(f"{self.get_text('alert_areas')}: {day.areas}")
            print('='*30)
    
    def display_report(self, report: WeatherReport):
        print('\n' + '='*30)
        self.display_message(
            'report_title',
            city=report.city.title(),
            date1=report.start_date,
            date2=report.end_date
        )
        print(self.get_text('report_max_temp', max_temp_period=report.period_max_temp))
        print(self.get_text('report_min_temp', min_temp_period=report.period_min_temp))
        print(self.get_text('report_total_precip', total_precip=report.total_precip))
        print(self.get_text('report_rainy_days', num_rainy_days=report.rainy_days))
        print(self.get_text('report_avg_temp', final_avg_temp=report.avg_temp))
        print(self.get_text('report_avg_umidity', final_avg_humidity=report.avg_humidity))
        print('='*30)
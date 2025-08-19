# weather_display contém as principais funções do menu, no geral usando chamadas da API para obter informações
# e os dicionários para gerenciar as traduções de textos exibidos
from traducao import translations
from datetime import datetime, timedelta
from .api_service import get_weather_data, get_historical_data
from .feedback import Feedback

ALL_FEEDBACKS = []

# Função para exibir a previsão do tempo
def previsao(language):
    try:
        city = input(translations[language]['enter_city'])
        period = input(translations[language]['enter_period'])
        if period not in ['1', '3', '7']:
            print(translations[language]['invalid_period'])
            return
        # API recebe a cidade, o periodo da previsão e o idioma e retorna um Json com as informações
        weather_data = get_weather_data(city, period, language) 

        # esse for vai percorrer o conjunto de informações guardados em weather_data printando o que a gente quer
        count = 0
        print(f'{translations[language]['text_city']}: {city.title()}')
        for day_data in weather_data['forecast']['forecastday']:
            print('\n' + '='*30)
            count+=1
            print(f'Dia {count}:')
            # As informações do Json também estão em um dicionário, por isso usamos esse formato pra acessar os dados
            print(f'{translations[language]['day']}: {day_data['date']}') 
            print(f'{translations[language]['max_temp']}: {day_data['day']['maxtemp_c']}°')
            print(f'{translations[language]['min_temp']}: {day_data['day']['mintemp_c']}°')
            print(f'{translations[language]['conditions']}: {day_data['day']['condition']['text']}')
            print(f'{translations[language]['sunrise']}: {day_data['astro']['sunrise']}')
            print(f'{translations[language]['sunset']}: {day_data['astro']['sunset']}')
            print('='*30)

        option = input(translations[language]['consult_another_city'])
        if option == 'c':
            previsao(language)
        elif option == 'm':
            return
        else:
            print(translations[language]['invalid_input'])
            return
    except Exception:
        print(translations[language]['invalid_input'])
        return

# Função para exibir o tempo atual
def tempo(language):
    try:
        print('\n' + '='*30)
        print(translations[language]['select_feature'])
        print(translations[language]['my_location'])
        print(translations[language]['another_location'])
        print('='*30)
        option = input(translations[language]['choose_option'])

        if option == '1':
            query = "auto:ip"
        elif option == '2':
            query = input(translations[language]['enter_city'])
        else:
            print(translations[language]['invalid_input'])
            return

        # realizamos a requisição passando o ip da máquina pra pegar a localização atual e 1 para pegar os dados de hoje
        weather_data = get_weather_data(query, 1, language)
        city = weather_data['location']['name']

        print('\n' + '='*30)
        print(f'{translations[language]['weather_in_city']} {city.title()}')
        print(f'{translations[language]['conditions']}: {weather_data['current']['temp_c']}°')
        print(f'{translations[language]['conditions']}: {weather_data['current']['condition']['text']}')
        print(f'{translations[language]['humidity']}: {weather_data['current']['humidity']}%')
        print(f'{translations[language]['wind_speed']}: {weather_data['current']['wind_kph']}km/h')
        print(f'{translations[language]['precipitation']}: {weather_data['current']['precip_mm']}mm')
        print('='*30)
        
        option = input(translations[language]['consult_another_city'])
        if option == 'c':
            tempo(language)
        elif option == 'm':
            return
        else:
            print(translations[language]['invalid_input'])
            return
    except Exception:
        print(translations[language]['invalid_input'])
        return

# Função para exibir alertas climáticos
def alertas(language):
    try:
        city = input(translations[language]['enter_alert_city'])
        weather_data = get_weather_data(city, 7, language)

        # verifica se há alertas no dicionário retornado pela API                               
        if 'alerts' in weather_data:
            if weather_data['alerts']['alert']:
                print(f'{translations[language]['weather_alerts']} : {city.title()}')
                for alert in weather_data['alerts']['alert']: 
                    print('\n' + '='*30)
                    print(f"{translations[language]['alert_title']}: {alert.get('headline', 'N/A')}")
                    print(f"{translations[language]['alert_description']}: {alert.get('desc', 'N/A')}")
                    print(f"{translations[language]['alert_severity']}: {alert.get('severity', 'N/A')}")
                    print(f"{translations[language]['alert_urgency']}: {alert.get('urgency', 'N/A')}")
                    print(f"{translations[language]['alert_areas']}: {alert.get('areas', 'N/A')}")
                    print('='*30)
            else:
                print('\n' + '='*30)
                print(translations[language]['no_alerts'])
                print('='*30)
    except Exception:
        print(translations[language]['invalid_input'])
        return

# Função para exibir o histórico do tempo
def history(language):
    try:
        print('\n' + '='*30)
        city = input(translations[language]['enter_city'])
        print(translations[language]['historical_note'])
        date = input(translations[language]['enter_date'])
        print('='*30)

        historical_data = get_historical_data(city, date, language)
        day_data = historical_data['forecast']['forecastday'][0]

        print('\n' + '='*30)
        print(f'{translations[language]['historical_weather']}: {day_data['date']} em {city.title()}')
        print(f'{translations[language]['max_temp']}: {day_data['day']['maxtemp_c']}°')
        print(f'{translations[language]['min_temp']}: {day_data['day']['mintemp_c']}°')
        print(f'{translations[language]['conditions']}: {day_data['day']['condition']['text']}')
        print(f'{translations[language]['total_precip']}: {day_data['day']['totalprecip_mm']}mm')
        print(f'{translations[language]['max_wind_speed']}: {day_data['day']['maxwind_kph']}km/h')
        print(f'{translations[language]['avg_humidity']}: {day_data['day']['avghumidity']}%')
        print(f'{translations[language]['sunrise']}: {day_data['astro']['sunrise']}')
        print(f'{translations[language]['sunset']}: {day_data['astro']['sunset']}')
        print('='*30)
        
        option = input(translations[language]['consult_another_city'])
        if option == 'c':
            history(language)
        elif option == 'm':
            return
        else:
            print(translations[language]['invalid_input'])
            return
    except Exception:
        print(translations[language]['invalid_input'])
        return

# Função para enviar feedback
def feedback(language):
    try:
        print(translations[language]['feedback_menu'])
        option = input(translations[language]['feedback_choice'])

        if option == '1':
            location = input(translations[language]['enter_location'])
            condition = input(translations[language]['enter_condition'])
            date = input(translations[language]['enter_feedback_date'])
            comment = input(translations[language]['enter_comment'])

            new_feedback = Feedback(condition, location, date, comment)
            ALL_FEEDBACKS.append(new_feedback)

            option1 = input(translations[language]['feedback_another'])
            
            if option1 == 'f':
                feedback(language)
            elif option1 == 'm':
                return
        elif option == '2':
            view_feedback(language)
        else:
            print('Opção Inválida')
    except Exception:
        print(translations[language]['invalid_input'])
        return

# Função para ver os Feedbacks
def view_feedback(language):
    try:
        if not ALL_FEEDBACKS:
            print(translations[language]['no_feedbacks'])
        else:
            cont = 0
            for x in ALL_FEEDBACKS:
                cont += 1
                print('\n' + '='*30)
                print(f'{translations[language]['feedback_number']} {cont}:')
                print(x)
                print('='*30)
    except Exception:
        print(translations[language]['invalid_input'])
        return

# Função para gerar Relatórios
MAX_DAYS_FOR_REPORT = 30 

def report(language):
    try:
        # Usando traduções para as mensagens de input
        city = input(translations[language]['report_city_prompt'])
        print(translations[language]['report_dates_prompt'])
        print(translations[language]['report_date_format_prompt'])
        date1 = input(translations[language]['report_date1_prompt'])
        date2 = input(translations[language]['report_date2_prompt'])

        date1_obj = datetime.strptime(date1, '%Y-%m-%d').date()
        date2_obj = datetime.strptime(date2, '%Y-%m-%d').date()

        if date1_obj > date2_obj:
            print(translations[language]['report_date_error_order'])
            return

        num_days = (date2_obj - date1_obj).days + 1 

        if num_days > MAX_DAYS_FOR_REPORT:
            print(translations[language]['report_date_error_limit'].format(MAX_DAYS_FOR_REPORT=MAX_DAYS_FOR_REPORT))
            return
        
        current_date = date1_obj
        
        # Variáveis para acumular os dados
        max_temp_period = float('-inf')  # Inicializa com o menor valor possível
        min_temp_period = float('inf')   # Inicializa com o maior valor possível
        total_precip = 0.0
        num_rainy_days = 0
        total_avg_temp = 0.0
        total_avg_umidity = 0.0
        num_days_with_data = 0

        while current_date <= date2_obj:
            date_str = current_date.isoformat() 
            historical_data = get_historical_data(city, date_str, language)

            if historical_data:
                day_data = historical_data['forecast']['forecastday'][0]
                day_summary = day_data['day'] # Acessa o dicionário 'day' para simplificar

                # Lógica para encontrar a temperatura máxima e mínima do período
                if day_summary['maxtemp_c'] > max_temp_period:
                    max_temp_period = day_summary['maxtemp_c']
                if day_summary['mintemp_c'] < min_temp_period:
                    min_temp_period = day_summary['mintemp_c']

                # Acumula os valores para as médias e totais
                total_precip += day_summary['totalprecip_mm']
                total_avg_temp += day_summary['avgtemp_c']
                total_avg_umidity += day_summary['avghumidity']
                
                # Conta os dias chuvosos
                if day_summary['totalprecip_mm'] > 0:
                    num_rainy_days += 1
                
                num_days_with_data += 1 
            
            current_date += timedelta(days=1) 
        
        print('\n' + '='*30)
        print(translations[language]['report_title'].format(city=city.title(), date1=date1, date2=date2))
        
        if num_days_with_data > 0:
            final_avg_temp = total_avg_temp / num_days_with_data
            final_avg_humidity = total_avg_umidity / num_days_with_data
            
            print(translations[language]['report_max_temp'].format(max_temp_period=max_temp_period))
            print(translations[language]['report_min_temp'].format(min_temp_period=min_temp_period))
            print(translations[language]['report_total_precip'].format(total_precip=total_precip))
            print(translations[language]['report_rainy_days'].format(num_rainy_days=num_rainy_days))
            print(translations[language]['report_avg_temp'].format(final_avg_temp=final_avg_temp))
            print(translations[language]['report_avg_umidity'].format(final_avg_humidity=final_avg_humidity))
        else:
            print(translations[language]['report_no_data'])
            
        print('='*30)
        
    except ValueError:
        print(translations[language]['report_invalid_date_format'])
        return
    except Exception:
        print(translations[language]['invalid_input'])
        return
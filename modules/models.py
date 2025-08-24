class CurrentWeather:
    def __init__(self, city, temp_c, humidity, wind_kph, precip_mm, condition_text):
        self.city = city
        self.temp_c = temp_c
        self.humidity = humidity
        self.wind_kph = wind_kph
        self.precip_mm = precip_mm
        self.condition = condition_text

    @classmethod
    def from_dict(cls, data):
        current_data = data.get('current', {})
        location_data = data.get('location', {})
        return cls(
            city=location_data.get('name'),
            temp_c=current_data.get('temp_c'),
            humidity=current_data.get('humidity'),
            wind_kph=current_data.get('wind_kph'),
            precip_mm=current_data.get('precip_mm'),
            condition_text=current_data.get('condition', {}).get('text')
        )

class ForecastDay:
    def __init__(self, date, max_temp_c, min_temp_c, condition_text, sunrise, sunset):
        self.date = date
        self.max_temp_c = max_temp_c
        self.min_temp_c = min_temp_c
        self.condition = condition_text 
        self.sunrise = sunrise
        self.sunset = sunset

    @classmethod
    def from_dict(cls, day_forecast_data):
        day_data = day_forecast_data.get('day', {})
        astro_data = day_forecast_data.get('astro', {})
        
        date = day_forecast_data.get('date')
        maxtemp = day_data.get('maxtemp_c')
        mintemp = day_data.get('mintemp_c')
        cond = day_data.get('condition', {}).get('text')
        sunrise = astro_data.get('sunrise')
        sunset = astro_data.get('sunset')

        return cls(date=date, max_temp_c=maxtemp, min_temp_c=mintemp, condition_text=cond, sunrise=sunrise, sunset=sunset)
    
class HistoricalDay:
    def __init__(self, date, max_temp, min_temp, condition, total_precip, max_wind, avg_humidity, avg_temp, sunrise, sunset):
        self.date = date
        self.max_temp = max_temp
        self.min_temp = min_temp
        self.condition = condition
        self.total_precip = total_precip
        self.max_wind_speed = max_wind
        self.avg_humidity = avg_humidity
        self.avg_temp = avg_temp
        self.sunrise = sunrise
        self.sunset = sunset

    @classmethod
    def from_dict(cls, data):
        day_forecast_data = data.get('forecast', {}).get('forecastday', [{}])[0]
        day_data = day_forecast_data.get('day', {})
        astro_data = day_forecast_data.get('astro', {})
        return cls(
            date=day_forecast_data.get('date'),
            max_temp=day_data.get('maxtemp_c'),
            min_temp=day_data.get('mintemp_c'),
            condition=day_data.get('condition', {}).get('text'),
            total_precip=day_data.get('totalprecip_mm'),
            max_wind=day_data.get('maxwind_kph'),
            avg_humidity=day_data.get('avghumidity'),
            avg_temp=day_data.get('avgtemp_c'),
            sunrise=astro_data.get('sunrise'),
            sunset=astro_data.get('sunset')
        )

class Feedback:
    def __init__(self, condition, location, date, comment):
        self.location = location
        self.condition = condition
        self.date = date
        self.comment = comment

    def __str__(self):
        return (f"\nLocal: {self.location}\nCondição: {self.condition}\n"
                f"Data: {self.date}\nComentário: {self.comment}")

class AlertWeather:
    def __init__(self, headline, desc, severity, urgency, areas):
        self.headline = headline
        self.desc = desc
        self.severity = severity
        self.urgency = urgency
        self.areas = areas

    @classmethod
    def from_dict(cls, alert_data):
        return cls(
            headline=alert_data.get('headline', 'N/A'),
            desc=alert_data.get('desc', 'N/A'),
            severity=alert_data.get('severity', 'N/A'),
            urgency=alert_data.get('urgency', 'N/A'),
            areas=alert_data.get('areas', 'N/A')
        )
    
class WeatherReport:
    def __init__(self, city, start_date, end_date, period_max_temp, period_min_temp, total_precip, rainy_days, avg_temp, avg_humidity):
        self.city = city
        self.start_date = start_date
        self.end_date = end_date
        self.period_max_temp = period_max_temp
        self.period_min_temp = period_min_temp
        self.total_precip = total_precip
        self.rainy_days = rainy_days
        self.avg_temp = avg_temp
        self.avg_humidity = avg_humidity
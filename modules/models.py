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
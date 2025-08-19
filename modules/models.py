class CurrentWeather:
    def __init__(self, temp_c, humidity, wind_kph, precip_mm, condition_text):
        self.temp_c = temp_c
        self.humidity = humidity
        self.wind_kph = wind_kph
        self.precip_mm = precip_mm
        self.condition_text = condition_text

    @classmethod
    def from_dict(cls, data):
        cls.data = data
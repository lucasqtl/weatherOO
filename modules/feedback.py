# Classe para armazenar feedback do usuário sobre as condições climáticas
class Feedback:

    def __init__(self, condition, location, date, comment):
        self.location = location
        self.condition = condition
        self.date = date
        self.comment = comment

    def __str__(self):
        return f"Local: {self.location}\nCondição: {self.condition}\nData: {self.date}\nComentário: {self.comment}\n"
    
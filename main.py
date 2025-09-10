from modules.ui import UIManager
from modules.services import ApiService
from modules.features import Forecast, Current, History, Feedback, Alert, Report

class WeatherApp:
    def __init__(self):
        self.ui = UIManager() 
        self.api = ApiService()
        self.feedbacks_list = []
        
       
        self.features = {
            "1": Forecast(self.api, self.ui),
            "2": Current(self.api, self.ui),
            "3": History(self.api, self.ui),
            "4": Feedback(self.api, self.ui, self.feedbacks_list),
            "5": Report(self.api, self.ui),
            "6": Alert(self.api, self.ui),
        }
    
    def run(self):
        while True:
            self.ui.display_main_menu()
            option = self.ui.get_user_input('choose_option')

            if option == '0':
                break
            
            if option == '7':
                new_lang = input('Escolha um Idioma (pt, en, es): ').lower()
                if not self.ui.set_language(new_lang):
                    self.ui.display_message('invalid_input')
                continue 

            feature_to_run = self.features.get(option)

            if feature_to_run:
                feature_to_run.execute()
            else:
                self.ui.display_message('invalid_input')

if __name__ == '__main__':
    app = WeatherApp()
    app.run()
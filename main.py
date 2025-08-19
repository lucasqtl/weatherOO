from traducao import translations, display_menu
from modules.weather_display import previsao, tempo, alertas, history, feedback, report


language = "pt" 

# a main é o menu de seleção e chama as funções de acordo com a opção selecionada
if __name__ == '__main__':
    print('\n' + '='*30)
    print('Português: pt')
    print('Inglês: en')
    print('Espanhol: es')
    language = input('Escolha um Idioma: ').lower()
    print('='*30)

    if language not in translations:
        print("Idioma inválido. Usando Português (pt) por padrão.")
        language = 'pt'


    while True:
        display_menu(language)
        
        try:
            op = int(input(translations[language]['choose_option']))

            if op == 0:
                break
            elif op == 1:
                previsao(language)

            elif op == 2:
                tempo(language)
                
            elif op == 3:
                history(language)

            elif op == 4:
                feedback(language)
                
            elif op == 5:
                report(language)

            elif op == 6:
                alertas(language)

            elif op == 7:
                print('\n' + '='*30)
                print('Português: pt')
                print('Inglês: en')
                print('Espanhol: es')
                new_language = input('Escolha um Idioma: ').lower()
                print('='*30)
                if new_language in translations:
                    language = new_language
                else:
                    print(f"Idioma '{new_language}' não suportado. Mantendo o idioma atual.")
            else:
                print("Opção inválida. Por favor, tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
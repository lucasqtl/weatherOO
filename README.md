## Weather Forecasting System- Previsão e Análise do Tempo via Linha de Comando

### Introdução

O Weather Forecasting System é um projeto de aplicação de linha de comando (CLI) desenvolvido em Python para fornecer informações meteorológicas detalhadas, como previsão do tempo, dados históricos, alertas e análises climáticas.

---

### Funcionalidades Implementadas

O projeto cobre as seguintes funcionalidades principais, conforme o escopo original:

* 1 - Geração de Previsão: Fornece a previsão do tempo para os próximos 1, 3 ou 7 dias com base em uma cidade inserida pelo usuário. A funcionalidade exibe a temperatura máxima e mínima, condições climáticas, horários do nascer e pôr do sol para cada dia.

* 2 - Serviços de Localização do Usuário: Detecta a localização atual do usuário via endereço IP para fornecer a situação climática em tempo real. Os dados incluem temperatura, umidade, velocidade do vento e precipitação. Você também pode consultar os dados do clima atual inserindo o nome da cidade.

* 3 - Acesso a Dados Meteorológicos Históricos: Permite consultar as condições climáticas de uma cidade em uma data específica, com dados disponíveis de 1 ano atrás contando da data atual.

* 4 - Feedback e Relatórios do Usuário: Oferece um sistema de feedback simples. O usuário pode registrar a condição do clima de sua localização e visualizá-la durante a mesma sessão de uso da aplicação.

* 5 - Análise e Relatórios Climáticos: Gera um relatório resumido de um período de até 30 dias para uma cidade específica. A análise inclui a temperatura média e extrema do período, precipitação total e o número de dias chuvosos.

* 6 - Sistema de Alerta para Clima Severo: Consulta a API para verificar a existência de alertas climáticos em uma determinada cidade. Caso existam, o programa exibe o título, a severidade e a descrição dos alertas para os próximos 7 dias.

* 7 - Suporte a Múltiplos Idiomas: O menu e todas as mensagens do programa estão disponíveis em Português, Inglês e Espanhol, com base em um dicionário de traduções e na escolha do usuário.

* Coleta de Dados Meteorológicos: A agregação de dados é realizada de forma transparente e eficiente, utilizando a API da WeatherAPI.com, que serve como nossa única fonte de dados. Essa não está definida no menu, pois não é uma funcionalidade de acesso direto, mas o seu uso está implicito para o funcionamento do programa

---

### Funcionalidades Não Implementadas e Justificativa

As seguintes funcionalidades não foram implementadas, pois a inviabilidade técnica ou a complexidade excessiva para uma aplicação de linha de comando as tornaria incompatíveis com a proposta e o escopo do projeto:

Mapas Interativos de Clima: A exibição de mapas dinâmicos e interativos é uma tarefa exclusiva para aplicações com interface gráfica (GUI). Em um ambiente de terminal, a renderização de imagens e a interação com elementos visuais de um mapa não são possíveis. A alternativa seria abrir uma URL no navegador, mas isso foge do contexto de uma experiência puramente via CLI.

Widgets de Clima Personalizáveis: A personalização de widgets é uma funcionalidade típica de websites, aplicativos desktop ou mobile, que possuem interfaces gráficas para arrastar, redimensionar e exibir informações de forma visual. Embora a lógica de "personalizar" possa ser simulada com configurações em texto no terminal, a ausência de uma interface visual para exibir um "widget" de forma compacta e permanente na tela tornaria a funcionalidade sem propósito.

---

### Pré-requisitos e Instalação

Para rodar este projeto, você precisará ter o Python instalado e uma API Key da WeatherAPI.com.

OBS: Para a correção desse trabalho, vou deixar disponibilizada a minha chave de API já no código pra facilitar o processo. A Key é válida até o dia 15/08/2025, caso a correção esteja ocorrendo após esse periodo, recomendo a criação de uma nova chave.

Obtenha sua API Key:

Crie uma conta gratuita em https://www.weatherapi.com/.

No seu painel, copie a API Key fornecida.

Clone o Repositório:
```
git clone https://github.com/lucasqtl/weather.git
cd weather
```

Crie um Ambiente Virtual (Altamente Recomendado):
```
python -m venv .venv

Ative o ambiente virtual
No Windows (PowerShell): .\ .venv\Scripts\Activate.ps1
No Windows (Cmd): .venv\Scripts\activate.bat
No macOS/Linux: source .venv/bin/activate
```

Instale as Dependências:
```
pip install requests
```

Configure a API Key:

Abra o arquivo modules/api_service.py.

Substitua "SUA_CHAVE_AQUI" pelo valor da sua API Key.
```

modules/api_service.py
API_KEY = "SUA_CHAVE_AQUI"  # Insira sua API Key aqui
```

---

### Como Usar o Programa

Para iniciar a aplicação, com o ambiente virtual ativado, execute o seguinte comando no terminal:

```
python main.py
```

O programa apresentará um menu principal onde você pode escolher o idioma e, em seguida, uma das funcionalidades implementadas.

#### Guia de Funcionalidades:

Previsão do Tempo (Opção 1): Digite o nome da cidade para ver a previsão dos próximos 1, 3 ou 7 dias.

Dados do Clima Atual (Opção 2): O programa detectará sua localização por IP e exibirá as condições atuais ou você pode digitar a cidade que deseja consultar.

Dados Históricos (Opção 3): Digite o nome da cidade e uma data no formato yyyy-MM-dd para ver o clima passado.

Feedback (Opção 4): Envie um feedback sobre o clima ou visualize os feedbacks enviados durante a sessão.

Análise Climática (Opção 5): Digite uma cidade e um intervalo de até 30 dias para receber um relatório resumido.

Alertas (Opção 6): Verifique se há alertas de clima severo para uma cidade.

Selecionar Idioma (Opção 7): Altere o idioma do menu e das mensagens.

---
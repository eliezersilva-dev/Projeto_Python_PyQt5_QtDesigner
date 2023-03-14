from PyQt5 import uic, QtWidgets, QtGui
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from time import sleep
import json
from datetime import date, datetime
import requests

global textos
global capitais
global estados


def buscar_noticias():

    options = Options()
    options.add_argument('--headless')
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico, options=options)
    navegador.get('https://jovempan.com.br/')

    sleep(1)

    site = BeautifulSoup(navegador.page_source, 'html.parser')
    noticia = site.find('div', attrs={'class': 'row row-flex'})
    titulos = noticia.findAll('p', attrs={'class': 'title'})

    global textos
    textos = []
    for i in titulos:
        textos.append(i.text)


def chamar_atualizar():
    import random
    print(textos[random.choice(range(len(textos)))])
    tela_noticias.label_noticias.setText(textos[random.choice(range(len(textos)))])


def montar_listas_capitais():
    global capitais
    global estados
    with open('arquivos/previsoes_capitais_brasil.txt', 'r', encoding="utf8") as arquivo_previsoes:
        capitais = arquivo_previsoes.read()
        capitais = json.loads(capitais)
        print(capitais)
    with open('arquivos/capitais_estados.txt', 'r', encoding="utf8") as arquivo_capitais:
        estados = arquivo_capitais.read()
        estados = json.loads(estados)
        print(estados)


def previsao_capital():
    consulta = tela_noticias.comboBox.currentText()
    print(consulta)

    if consulta == 'CAPITAIS':
        tela_noticias.label_previsao.setText('Selecione uma Capital')
        tela_noticias.label_capital_estado.setText('Capital/Estado')
    else:
        print(consulta)
        for i, j in estados.items():
            if consulta in i:
                estado = j
                tela_noticias.label_capital_estado.setText(f'{consulta}/{estado}')
                print(f'{consulta}/{estado}')

        consulta = capitais[consulta]
        print(consulta)

        previsao = requests.get(consulta)
        previsao = previsao.json()

        data = previsao['daily']
        data = data['time']
        data = data[0]
        data = datetime.strptime(data, '%Y-%m-%d').date()
        data = datetime.strftime(data, '%d/%m/%Y')
        print(f'Data: {data}')

        temp_min = previsao['daily']
        temp_min = temp_min['temperature_2m_min']
        temp_min = temp_min[0]
        print(f'Temperatura Mínima: {temp_min}')

        temp_max = previsao['daily']
        temp_max = temp_max['temperature_2m_max']
        temp_max = temp_max[0]
        print(f'Temperatura Máxima: {temp_max}')

        precipitacao = previsao['daily']
        precipitacao = precipitacao['precipitation_sum']
        precipitacao = precipitacao[0]
        print(f'Precipitação de chuva última hora: {precipitacao} mm')

        tela_noticias.label_previsao.setText(f'Temperatura Mínima: {temp_min}\n'
                                             f'Temperatura Máxima: {temp_max}\n'
                                             f'Precipitação de chuva última hora: {precipitacao} mm')

        data_hora = datetime.now()
        print(f'{data_hora.day}/{data_hora.month}/{data_hora.year}\n'
              f'{data_hora.hour}:{data_hora.minute}')
        tela_noticias.label_data_hora.setText((f'{data_hora.day}/{data_hora.month}/{data_hora.year}\n'
                                               f'{data_hora.hour}:{data_hora.minute}'))




app = QtWidgets.QApplication([])
tela_noticias = uic.loadUi('tela_noticias.ui')
tela_noticias.setWindowTitle('Notícias')
tela_noticias.setWindowIcon(QtGui.QIcon('imagens/informativo_icon.png'))

tela_noticias.btn_atualizar.clicked.connect(chamar_atualizar)
tela_noticias.btn_tempo.clicked.connect(previsao_capital)

buscar_noticias()
montar_listas_capitais()

tela_noticias.show()
app.exec()

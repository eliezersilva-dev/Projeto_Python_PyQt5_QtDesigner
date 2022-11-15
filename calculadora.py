from PyQt5 import uic, QtWidgets, QtGui

valores = ''


def limpar_tela():
    global valores
    tela_calculadora.label_display.setText('0')
    valores = ''


def botao_neg_pos():
    global valores
    sinal_neg = '-'
    if valores == '':
        pass
    elif valores[0] != '-':
        valores = sinal_neg + valores
    elif valores[0] == '-':
        valores = valores[1:]
    tela_calculadora.label_display.setText(valores)


def botao_del():
    global valores
    valores = valores[:-1]
    tela_calculadora.label_display.setText(valores)


def botao_dividir():
    global valores
    if valores[-1] != '+' and valores[-1] != '-' \
            and valores[-1] != '/' and valores[-1] != '*':
        valores += '/'
    tela_calculadora.label_display.setText(valores)


def botao_sete():
    global valores
    tela_calculadora.label_display.setText('7')
    if len(valores) <= 14:
        valores += tela_calculadora.label_display.text()
    tela_calculadora.label_display.setText(valores)


def botao_oito():
    global valores
    tela_calculadora.label_display.setText('8')
    if len(valores) <= 14:
        valores += tela_calculadora.label_display.text()
    tela_calculadora.label_display.setText(valores)


def botao_nove():
    global valores
    tela_calculadora.label_display.setText('9')
    if len(valores) <= 14:
        valores += tela_calculadora.label_display.text()
    tela_calculadora.label_display.setText(valores)


def botao_multiplicar():
    global valores
    if valores[-1] != '+' and valores[-1] != '-' \
            and valores[-1] != '/' and valores[-1] != '*':
        valores += '*'
    tela_calculadora.label_display.setText(valores)


def botao_quatro():
    global valores
    tela_calculadora.label_display.setText('4')
    if len(valores) <= 14:
        valores += tela_calculadora.label_display.text()
    tela_calculadora.label_display.setText(valores)


def botao_cinco():
    global valores
    tela_calculadora.label_display.setText('5')
    if len(valores) <= 14:
        valores += tela_calculadora.label_display.text()
    tela_calculadora.label_display.setText(valores)


def botao_seis():
    global valores
    tela_calculadora.label_display.setText('6')
    if len(valores) <= 14:
        valores += tela_calculadora.label_display.text()
    tela_calculadora.label_display.setText(valores)


def botao_subtrair():
    global valores
    if valores[-1] != '+' and valores[-1] != '-' \
            and valores[-1] != '/' and valores[-1] != '*':
        valores += '-'
    tela_calculadora.label_display.setText(valores)


def botao_um():
    global valores
    tela_calculadora.label_display.setText('1')
    if len(valores) <= 14:
        valores += tela_calculadora.label_display.text()
    tela_calculadora.label_display.setText(valores)


def botao_dois():
    global valores
    tela_calculadora.label_display.setText('2')
    if len(valores) <= 14:
        valores += tela_calculadora.label_display.text()
    tela_calculadora.label_display.setText(valores)


def botao_tres():
    global valores
    tela_calculadora.label_display.setText('3')
    if len(valores) <= 14:
        valores += tela_calculadora.label_display.text()
    tela_calculadora.label_display.setText(valores)


def botao_somar():
    global valores
    if valores[-1] != '+' and valores[-1] != '-'\
            and valores[-1] != '/' and valores[-1] != '*':
        valores += '+'
    tela_calculadora.label_display.setText(valores)


def botao_zero():
    global valores
    tela_calculadora.label_display.setText('0')
    if len(valores) <= 14:
        valores += tela_calculadora.label_display.text()
    tela_calculadora.label_display.setText(valores)


def botao_ponto():
    global valores
    tela_calculadora.label_display.setText('.')
    if len(valores) <= 14:
        if '.' not in valores:
            valores += tela_calculadora.label_display.text()
    tela_calculadora.label_display.setText(valores)


def botao_igual():
    global valores
    valores = str(eval(valores))
    tela_calculadora.label_display.setText(valores)


def botao_voltar():
    tela_calculadora.close()


app = QtWidgets.QApplication([])
tela_calculadora = uic.loadUi('tela_calculadora.ui')
tela_calculadora.setWindowIcon(QtGui.QIcon('imagens/calculadora-icon.png'))
tela_calculadora.setWindowTitle('Calculadora')

tela_calculadora.btn_C.clicked.connect(limpar_tela)
tela_calculadora.btn_positivoNegativo.clicked.connect(botao_neg_pos)
tela_calculadora.btn_del.clicked.connect(botao_del)
tela_calculadora.btn_dividir.clicked.connect(botao_dividir)
tela_calculadora.btn_sete.clicked.connect(botao_sete)
tela_calculadora.btn_oito.clicked.connect(botao_oito)
tela_calculadora.btn_nove.clicked.connect(botao_nove)
tela_calculadora.btn_multiplicar.clicked.connect(botao_multiplicar)
tela_calculadora.btn_quatro.clicked.connect(botao_quatro)
tela_calculadora.btn_cinco.clicked.connect(botao_cinco)
tela_calculadora.btn_seis.clicked.connect(botao_seis)
tela_calculadora.btn_subtrair.clicked.connect(botao_subtrair)
tela_calculadora.btn_um.clicked.connect(botao_um)
tela_calculadora.btn_dois.clicked.connect(botao_dois)
tela_calculadora.btn_tres.clicked.connect(botao_tres)
tela_calculadora.btn_somar.clicked.connect(botao_somar)
tela_calculadora.btn_zero.clicked.connect(botao_zero)
tela_calculadora.btn_ponto.clicked.connect(botao_ponto)
tela_calculadora.btn_igual.clicked.connect(botao_igual)
tela_calculadora.btn_voltar.clicked.connect(botao_voltar)

tela_calculadora.show()
app.exec()

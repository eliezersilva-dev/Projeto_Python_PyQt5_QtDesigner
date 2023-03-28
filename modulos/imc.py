from PyQt5 import uic, QtWidgets, QtGui


def chama_voltar():
    import main
    main.tela_main.show()
    app.exec()
    tela_imc.close()


def calcular_imc():
    peso = str(tela_imc.txt_peso.text())
    peso = peso.replace(',', '.')
    peso = float(peso)

    altura = str(tela_imc.txt_altura.text())
    altura = altura.replace(',', '.')
    altura = float(altura)

    imc = float(round(peso / (altura * altura), 2))

    if imc <= 18.5:
        tela_imc.label_mensagem.setText(' Classificação: Magreza - Obsidade: Grau 0 ')
    elif 18.5 < imc <= 24.9:
        tela_imc.label_mensagem.setText('  Classificação: Normal - Obsidade: Grau 0')
    elif 25.0 < imc <= 29.9:
        tela_imc.label_mensagem.setText(' Classificação: Sobrepeso - Obsidade: Grau I')
    elif 30.0 < imc <= 39.9:
        tela_imc.label_mensagem.setText('  Classificação: Obesidade - Obsidade: Grau II')
    elif imc >= 40.0:
        tela_imc.label_mensagem.setText(' Classificação: Obsidade Grave - Obsidade: Grau III')

    tela_imc.label_resultado.setText(f'  IMC: {imc}')


app = QtWidgets.QApplication([])
tela_imc = uic.loadUi('tela_imc.ui')
tela_imc.setWindowIcon(QtGui.QIcon('../imagens/imc-icon.png'))
tela_imc.setWindowTitle('Calcular IMC')

tela_imc.txt_peso.setInputMask('000,00')
tela_imc.txt_altura.setInputMask('0,00')

tela_imc.btn_calcular.clicked.connect(calcular_imc)
tela_imc.btn_voltar.clicked.connect(chama_voltar)

tela_imc.show()
app.exec()

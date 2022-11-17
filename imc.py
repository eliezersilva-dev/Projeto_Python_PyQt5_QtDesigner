from PyQt5 import uic, QtWidgets, QtGui


def calcular_imc():
    peso = tela_imc.txt_peso.text()
    peso = float(peso)
    altura = tela_imc.txt_altura.text()
    altura = float(altura)
    imc = peso / (altura**2)
    tela_imc.label_resultado.setText(f'IMC: {imc}')


app = QtWidgets.QApplication([])
tela_imc = uic.loadUi('tela_imc.ui')
tela_imc.setWindowIcon(QtGui.QIcon('imagens/imc-icon.png'))
tela_imc.setWindowTitle('Calcular IMC')

tela_imc.btn_calcular.clicked.connect(calcular_imc)

tela_imc.show()
app.exec()


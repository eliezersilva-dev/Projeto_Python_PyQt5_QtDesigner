from PyQt5 import uic, QtWidgets, QtGui


def chamar_sobre():
    print('cliquei em sobre')


def chamar_calculadora():
    import calculadora
    calculadora.tela_calculadora.show()
    calculadora.app.exec()


app = QtWidgets.QApplication([])
tela_main = uic.loadUi('tela_main.ui')
tela_main.setWindowIcon(QtGui.QIcon('imagens/application-icon.png'))
tela_main.setWindowTitle('Projetos Python')

tela_main.btn_sobre.clicked.connect(chamar_sobre)
tela_main.btn_calculadora.clicked.connect(chamar_calculadora)

tela_main.show()
app.exec()

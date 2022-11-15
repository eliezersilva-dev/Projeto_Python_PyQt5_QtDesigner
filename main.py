from PyQt5 import uic, QtWidgets, QtGui


def chamar_sobre():
    print('cliquei em sobre')


app = QtWidgets.QApplication([])
tela_main = uic.loadUi('tela_main.ui')
tela_main.setWindowIcon(QtGui.QIcon('imagens/favicon.png'))
tela_main.setWindowTitle('Projetos Python')
tela_main.btn_sobre.clicked.connect(chamar_sobre)


tela_main.show()
app.exec()


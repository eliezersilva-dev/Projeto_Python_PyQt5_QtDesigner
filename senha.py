from PyQt5 import uic, QtWidgets, QtGui

app = QtWidgets.QApplication([])
tela_senha = uic.loadUi('tela_senha.ui')
tela_senha.setWindowIcon(QtGui.QIcon('imagens/senha-icon.png'))
tela_senha.setWindowTitle('Gerar Senhas')


tela_senha.show()
app.exec()

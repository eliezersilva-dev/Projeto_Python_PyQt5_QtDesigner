from PyQt5 import uic, QtWidgets, QtGui



usuarios = [('Maria', '1234560'), ('João', 'abcdef'), ('Rose', '1ab2c3')]


def inserir_lista():
    print('cliquei')
    texto = str(usuarios[-1])
    texto = texto.replace('(', '')
    texto = texto.replace(')', '')
    texto = texto.replace("'", "")
    print(texto)
    tela_login.listWidget.addItem(texto)



app = QtWidgets.QApplication([])
tela_login = uic.loadUi('tela_login.ui')
tela_login.setWindowTitle('Tela Login')
tela_login.setWindowIcon(QtGui.QIcon(''))

tela_login.btn_cadastrar.clicked.connect(inserir_lista)




tela_login.show()
app.exec()


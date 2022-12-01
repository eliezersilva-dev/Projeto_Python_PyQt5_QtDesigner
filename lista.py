from PyQt5 import uic, QtWidgets, QtGui


def adicionar():
    texto = tela_lista.lineEdit.text()
    tela_lista.listWidget.addItem(texto)
    tela_lista.lineEdit.setText('')


def excluir():
    item = tela_lista.listWidget.takeItem(tela_lista.listWidget.currentRow())
    item = None


def limpar():
    tela_lista.listWidget.clear()


def marcar():
    try:
        item = tela_lista.listWidget.takeItem(tela_lista.listWidget.currentRow())
        f = item.font()
        f.setStrikeOut(True)
        item.setFont(f)
        texto = item
        item = None
        tela_lista.listWidget.insertItem(tela_lista.listWidget.currentRow(), texto)
    except:
        pass


def desmarcar():
    try:
        item = tela_lista.listWidget.takeItem(tela_lista.listWidget.currentRow())
        texto = item.text()
        item = None
        tela_lista.listWidget.insertItem(tela_lista.listWidget.currentRow(), texto)
    except:
        pass


app = QtWidgets.QApplication([])
tela_lista = uic.loadUi('tela_lista.ui')
tela_lista.setWindowIcon(QtGui.QIcon('imagens/calculadora-icon.png'))
tela_lista.setWindowTitle('Lista de Tarefas')

tela_lista.btn_adicionar.clicked.connect(adicionar)
tela_lista.btn_excluir.clicked.connect(excluir)
tela_lista.btn_limpar.clicked.connect(limpar)
tela_lista.btn_marcar.clicked.connect(marcar)
tela_lista.btn_desmarcar.clicked.connect(desmarcar)

tela_lista.show()
app.exec()

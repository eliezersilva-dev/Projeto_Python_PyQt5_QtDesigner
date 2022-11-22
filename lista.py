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

# *********************
# ponto de controle: implementar função marcar
# def marcar():
#     print('Marcado!')
#     item = tela_lista.listWidget.takeItem(tela_lista.listWidget.currentRow())
#     riscado = item.text()
#     item = None
#     print('item None ok')
#     print(riscado)
#     tela_lista.listWidget.takeItem(tela_lista.listWidget.currentRow(addItem('teste')))


    # riscado = riscado.setStrikeOut(True)
    # item.setFont(riscado)
    # print(item.font())
    # f = item.font()
    # f.setStrikeOut(True)
    # item.setFont(f)
    # font('text-decoration: line-through')




app = QtWidgets.QApplication([])
tela_lista = uic.loadUi('tela_lista.ui')
tela_lista.setWindowIcon(QtGui.QIcon('imagens/calculadora-icon.png'))
tela_lista.setWindowTitle('Lista de Tarefas')

tela_lista.btn_adicionar.clicked.connect(adicionar)
tela_lista.btn_excluir.clicked.connect(excluir)
tela_lista.btn_limpar.clicked.connect(limpar)
tela_lista.btn_marcar.clicked.connect(marcar)

tela_lista.show()
app.exec()

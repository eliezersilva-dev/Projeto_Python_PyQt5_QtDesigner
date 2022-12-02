import string
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox

geral = ''


def exibir_senha():
    import random

    if geral == '':
        QMessageBox.about(tela_senha, 'Alerta', 'Marque ao menos uma caixa.')
    else:
        quantidade_caracteres = int(tela_senha.label_qtd_caractere.currentText())
        senha = random.choices(geral, k=quantidade_caracteres)
        senha = str(senha)
        senha = senha.replace('[', '')
        senha = senha.replace(']', '')
        senha = senha.replace(',', '')
        senha = senha.replace("'", "")
        senha = senha.replace(' ', '')

        tela_senha.label_senha.setText(senha)


def botao_gerar():
    global geral
    geral = ''

    if tela_senha.checkBox_letrasMaius.isChecked():
        geral += string.ascii_uppercase
    if tela_senha.checkBox_letrasMinus.isChecked():
        geral += string.ascii_lowercase
    if tela_senha.checkBox_num.isChecked():
        geral += string.digits
    if tela_senha.checkBox_simbolos.isChecked():
        geral += '!@#$%&*._-'

    exibir_senha()


def botao_voltar():
    import main
    main.tela_main.show()
    app.exec()
    tela_senha.close()


app = QtWidgets.QApplication([])
tela_senha = uic.loadUi('tela_senha.ui')
tela_senha.setWindowTitle('Gerar Senhas')
tela_senha.setWindowIcon(QtGui.QIcon('imagens/senha-icon.png'))
tela_senha.label_imagem_cadeado.setStyleSheet('image: url(imagens/senha-imagem.png)')

tela_senha.btn_voltar.clicked.connect(botao_voltar)
tela_senha.btn_gerar.clicked.connect(botao_gerar)

tela_senha.show()
app.exec()

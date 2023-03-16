from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox

usuarios = {'Maria': '123456', 'João': 'abcdef', 'Rose': '1ab2c3'}


def login():
    tela_login.widget_imagem_cadeado.setStyleSheet('image: url(imagens/cadeado_fechado.jpg)')
    usuario_login = tela_login.lineEdit_usuario.text()
    senha_login = tela_login.lineEdit_senha.text()

    if not usuario_login in usuarios:
        QMessageBox.about(tela_login, 'Alerta', 'Usuário Inválido.')
    else:
        if usuarios[usuario_login] != senha_login:
            QMessageBox.about(tela_login, 'Alerta', 'Senha Inválida.')
        else:
            tela_login.widget_imagem_cadeado.setStyleSheet('image: url(imagens/cadeado_aberto.jpg)')

    tela_login.lineEdit_usuario.setText('')
    tela_login.lineEdit_senha.setText('')


def cadastrar():
    usuario = tela_login.lineEdit_usuario.text()
    senha = tela_login.lineEdit_senha.text()

    if usuario == '' or senha == '':
        QMessageBox.about(tela_login, 'Alerta', 'Insira usuário e senha.')
    if usuario in usuarios:
        QMessageBox.about(tela_login, 'Alerta', 'Usuário já Cadastrado.')
    else:
        tela_login.lineEdit_usuario.setText('')
        tela_login.lineEdit_senha.setText('')
        usuarios.update({usuario: senha})
        QMessageBox.about(tela_login, 'Mensagem', 'Cadastro realizado com sucesso.')
        tela_login.listWidget.addItem(f'{usuario}{+10 * " "}{senha}')


def voltar():
    import main
    main.tela_main.show()
    app.exec()
    tela_login.close()


app = QtWidgets.QApplication([])
tela_login = uic.loadUi('tela_login.ui')
tela_login.setWindowTitle('Tela Login')
tela_login.setWindowIcon(QtGui.QIcon('imagens/login_icon.png'))
tela_login.widget_imagem_cadeado.setStyleSheet('image: url(imagens/cadeado_fechado.jpg)')
tela_login.widget_imagem_usuario.setStyleSheet('image: url(imagens/imagem_usuario.png)')
tela_login.widget_imagem_login.setStyleSheet('image: url(imagens/imagem_login.png)')

tela_login.btn_cadastrar.clicked.connect(cadastrar)
tela_login.btn_login.clicked.connect(login)
tela_login.btn_voltar.clicked.connect(voltar)

tela_login.show()
app.exec()

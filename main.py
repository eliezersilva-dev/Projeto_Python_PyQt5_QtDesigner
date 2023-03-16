from PyQt5 import uic, QtWidgets, QtGui


def chamar_calculadora():
    import calculadora
    calculadora.tela_calculadora.show()
    calculadora.app.exec()
    tela_main.close()


def chamar_imc():
    import imc
    imc.tela_imc.show()
    imc.app.exec()
    tela_main.close()


def chamar_gerar_senha():
    import senha
    senha.tela_senha.show()
    senha.app.exec()
    tela_main.close()


def chamar_lista():
    import lista
    lista.tela_lista.show()
    lista.app.exec()
    tela_main.close()


def chamar_tela_login():
    import login
    login.tela_login.show()
    login.app.exec()
    tela_main.close()


def chamar_tela_noticia():
    login.app.exec()
    tela_main.close()


app = QtWidgets.QApplication([])
tela_main = uic.loadUi('tela_main.ui')
tela_main.setWindowIcon(QtGui.QIcon('imagens/application-icon.png'))
tela_main.setWindowTitle('Projetos Python')

tela_main.btn_calculadora.clicked.connect(chamar_calculadora)
tela_main.btn_imc.clicked.connect(chamar_imc)
tela_main.btn_gerarSenha.clicked.connect(chamar_gerar_senha)
tela_main.btn_lista.clicked.connect(chamar_lista)
tela_main.btn_telaLogin.clicked.connect(chamar_tela_login)
tela_main.btn_noticias.clicked.connect(chamar_tela_noticia)

tela_main.show()
app.exec()

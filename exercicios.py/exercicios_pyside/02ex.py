from PySide6.QtWidgets import QApplication ,QLabel, QPushButton, QWidget, QGridLayout, QMainWindow

iniciador = QApplication()

base = QWidget()
layout = QGridLayout()
janela = QMainWindow()

palavra = QLabel('opaaa')

botao1 = QPushButton('botao 1')
botao2 = QPushButton('botao 2')

layout.addWidget(palavra)
layout.addWidget(botao1)
layout.addWidget(botao2)

base.setLayout(layout)
janela.setCentralWidget(base)

menu = janela.menuBar()
menu.addMenu('menu 1')

janela.show()


iniciador.exec()

############### setWindowTitle ###############
############### layout.addWidget(botao3, 2, 1,1,3) ###############
############### setStyleSheet ############### outro jeito com o qt
############### statusBar ###############
############### showMessage ###############
############### addAction ###############

############### triggered.conect ###############


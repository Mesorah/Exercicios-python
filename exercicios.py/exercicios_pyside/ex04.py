from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QVBoxLayout, QMainWindow
from PySide6.QtGui import QFont, QAction
from PySide6.QtCore import Qt

app = QApplication()
janela = QMainWindow()
base = QWidget()
layout = QVBoxLayout()

font = QFont()
font.setPixelSize(90) # colocar uma fonte de 90, mas não ativa

label = QLabel('salve') # escreve na tela
label.setFont(font) # ativa ela, e coloca o tamanho como 90
label.setAlignment(Qt.AlignCenter) # quando aumentar ou diminuir
                                    # a tela, ela fica no meio

botao = QPushButton('slakkkkkkkkk')
botao.setFont(font)

layout.addWidget(label) # adiciona o label no layout
layout.addWidget(botao) # adiciona o botao no layout

base.setLayout(layout) # adiciona o layout como base

janela.setCentralWidget(base)
menu = janela.menuBar()
menu.addMenu('Arquivo')


janela.show() # mostra na tela

app.exec() # executa
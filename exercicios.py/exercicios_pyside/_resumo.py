from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QGridLayout, QMainWindow

iniciador = QApplication() # o que faz executar o codigo
palavra = QLabel('qualquer coisa') # cria uma guia com a palavra
botao = QPushButton('qualquer palavra') # cria uma guia com um botão com a palavra
base = QWidget() # cria uma base
layout = QGridLayout() # deixa criado um layout vertical
janela = QMainWindow() # cria um modo janela, tipo arquivos, salvar etc

janela.setWindowTitle('KKKKKKKKKKKKKKKKKKKKKK') #renomeia o nome do arquivo em cima 

layout.addWidget(palavra, 1, 1) # coloca o botão no layout
layout.addWidget(botao, 2, 2, 1, 5) # coloca a palavra no layout, linha, coluna, rowspan, colunspan

base.setLayout(layout) # seta o layout na base

janela.setCentralWidget(base) # deixa coma tela principal
menu = janela.menuBar() # cria o meno
primeiro_menu = menu.addMenu('opaa') # adiciona ele
primeira_acao = primeiro_menu.addAction('cria um tipo de sub menu') # quando aperta no menu aparece a ação

def slot(): # espera ser ativada pelo triggered
    print(123) # printa 123 quando for chamado

primeira_acao.triggered.connect(slot) # quando apertar no sub menu ira ativar a ação

status_bar = janela.statusBar() # cria o statusbar
status_bar.showMessage('nome em baixo') # cria um mone em baixo

janela.show() # inicia a guia

iniciador.exec() # a execução

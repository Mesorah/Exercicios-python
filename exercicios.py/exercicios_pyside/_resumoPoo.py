from PySide6.QtCore import Slot
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QGridLayout, QMainWindow, QPushButton, QWidget, QLabel

class MinhaJanela(QMainWindow):

    # inicia, parent não ira ser usado agora
    def __init__(self, parent=None):
        super().__init__(parent)

        # layout
        self.layout = QGridLayout()

        # base
        self.base = QWidget()
        self.base.setLayout(self.layout)

        # Fonte para o tamanho
        self.fonte = QFont()

        # definindo um título
        self.setWindowTitle('Título do arquivo')

        # definindo uma mensagem em baixo
        self.barra_de_status = self.statusBar()
        self.barra_de_status.showMessage('Primeira Barra de Status')

        # Barra do menu
        self.menu = self.menuBar()
        self.primeiro_menu = self.menu.addMenu('Primeiro menu')

        # Sub Menu
        self.primeira_acao = self.primeiro_menu.addAction('Primeiro sub menu')

        # Captando se a pessoa clicou no sub menu
        self.primeira_acao.triggered.connect(self.primeira_ativacao)

        # Criando a segunda ação
        self.segunda_acao = self.primeiro_menu.addAction('Segunda ação')

        # Tirando e colocando o ok no menu
        self.segunda_acao.setCheckable(True)

        # Quando mudar de estado ele chama a função
        self.segunda_acao.toggled.connect(self.ativado_ou_nao)

        # Quando passar o mouse em cima chama a função
        self.segunda_acao.hovered.connect(self.ativado_ou_nao)

        # Botões
        self.botao1 = QPushButton('Primeiro Botão')
        self.botao2 = self.cria_botao('Segundo Botão', 20)

        # Se o botão for precionado ele chama a função
        self.botao1.clicked.connect(self.printa_palavra)

        # palavras
        self.palavra1 = QLabel('Primeira palavra')

        # adicionando no layout
        self.layout.addWidget(self.botao1, 1,1,1,1)
        self.layout.addWidget(self.botao2)
        self.layout.addWidget(self.palavra1)

        # deixando como tela principal
        self.setCentralWidget(self.base)

    @Slot()
    def primeira_ativacao(self):
        self.barra_de_status.showMessage('Exec')

    @Slot()
    def ativado_ou_nao(self):
        print('Estou ativo?', self.segunda_acao.isChecked())

    def printa_palavra(self):
        print('Ai, isto machuca')

    def cria_botao(self,texto, tamanho=20):
        bt = QPushButton(texto)
        self.fonte.setPixelSize(tamanho)
        bt.setFont(self.fonte)
        return bt



if __name__ == '__main__':
    # o corpo da janela
    app = QApplication()

    janela = MinhaJanela()

    # fazendo aparecer na tela
    janela.show()
    app.exec()
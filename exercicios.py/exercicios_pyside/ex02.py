from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

app = QApplication()

font = QFont()
font.setPixelSize(90) # colocar uma fonte de 90, mas não ativa

label = QLabel('salve') # escreve na tela
label.setFont(font) # ativa ela, e coloca o tamanho como 90
label.setAlignment(Qt.AlignCenter) # quando aumentar ou diminuir
                                    # a tela, ela fica no meio
label.show() # mostra na tela

app.exec() # executa
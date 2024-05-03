import sys
from main_window import MainWindow
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QLabel, QApplication
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    # Iniciadores
    app = QApplication(sys.argv)
    window = MainWindow()

    # Delimita a fonta e o tamanho dela
    font = QFont()
    font.setPixelSize(50)

    # Adiciona um texto, e configura o tamanho dela
    label1 = QLabel('O meu texto')
    label1.setFont(font)
    window.addWidgetToVLayout(label1)

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Executores
    window.adjustFixedSize()
    window.show()
    app.exec()
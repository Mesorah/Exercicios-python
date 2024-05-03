from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        
        # Configura o layout básico
        self.structure = QWidget()
        self.vLayout = QVBoxLayout()
        self.structure.setLayout(self.vLayout)
        self.setCentralWidget(self.structure)

        # Coloca o Título do arquivo
        self.setWindowTitle('Calculadora')

    # Ajusta o tamanho da tela, e não deixa maximiza-la
    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    # Adiciona no vLayout
    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)
from re import T
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy
from PyQt5.QtCore import pyqtBoundSignal

class Calculadora(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle('Calculadora BrainStorm')
        self.setFixedSize(300, 400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.mostrador = QLineEdit()
        self.componentesDisplay()
        self.setBotoes()
        self.setStyleSheet(
            "* {background: white; color: black; font-size: 30px;}"
        )


    def componentesDisplay(self): 
        self.mostrador.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        self.grid.addWidget(self.mostrador, 0, 0, 1, 5)
        # self.mostrador.setDisabled(True)
        self.setCentralWidget(self.cw)
    

    def componentesBotoes(self, textoBotao: str, row, col, rowspan, colspan):
        self.botao = QPushButton(textoBotao, self)
        self.botao.clicked.connect(self.addNumerosDisplay)
        self.grid.addWidget(self.botao, row, col, rowspan, colspan)

    

    def setBotoes(self):
        self.componentesBotoes('0', 1, 0, 1, 1)
        self.componentesBotoes('1', 1, 1, 1, 1)
        self.componentesBotoes('2', 1, 2, 1, 1)
        self.componentesBotoes('3', 2, 0, 1, 1)
        self.componentesBotoes('4', 2, 1, 1, 1)
        self.componentesBotoes('5', 2, 2, 1, 1)
        self.componentesBotoes('6', 3, 0, 1, 1)
        self.componentesBotoes('7', 3, 1, 1, 1)
        self.componentesBotoes('8', 3, 2, 1, 1)
        self.componentesBotoes('1', 4, 0, 1, 1)


    def addNumerosDisplay(self):
        return self.mostrador.setText(
            self.mostrador.text() + self.botao.text()
        )

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()
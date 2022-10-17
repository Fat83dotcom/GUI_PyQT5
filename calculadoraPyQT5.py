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
        self.mostrador.setDisabled(True)
        self.setCentralWidget(self.cw)
    

    def componentesBotoes(self, botao, row, col, rowspan, colspan):
        botao.clicked.connect(
            lambda: self.mostrador.setText(
            self.mostrador.text() + botao.text()
            )
        )
        botao.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        self.grid.addWidget(botao, row, col, rowspan, colspan)


    

    def setBotoes(self):
        self.componentesBotoes(QPushButton('0', self), 1, 0, 1, 1)
        self.componentesBotoes(QPushButton('1', self), 1, 1, 1, 1)
        self.componentesBotoes(QPushButton('2', self), 1, 2, 1, 1)
        self.componentesBotoes(QPushButton('3', self), 2, 0, 1, 1)
        self.componentesBotoes(QPushButton('4', self), 2, 1, 1, 1)
        self.componentesBotoes(QPushButton('5', self), 2, 2, 1, 1)
        self.componentesBotoes(QPushButton('6', self), 3, 0, 1, 1)
        self.componentesBotoes(QPushButton('7', self), 3, 1, 1, 1)
        self.componentesBotoes(QPushButton('8', self), 3, 2, 1, 1)
        self.componentesBotoes(QPushButton('9', self), 4, 0, 1, 1)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()
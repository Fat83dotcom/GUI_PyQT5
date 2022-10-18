from cmath import sqrt
from re import T
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy
import math

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
            "* {background: white; color: black; font-size: 20px;}"
        )


    def componentesDisplay(self): 
        self.mostrador.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        self.grid.addWidget(self.mostrador, 0, 0, 1, 5)
        self.mostrador.setDisabled(True)
        self.setCentralWidget(self.cw)
    

    def componentesBotoes(self, botao, row, col, rowspan, colspan, func=None):
        self.grid.addWidget(botao, row, col, rowspan, colspan)
        botao.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        if not func:
            botao.clicked.connect(
                lambda: self.mostrador.setText(
                self.mostrador.text() + botao.text()
                )
            )
        else:
            botao.clicked.connect(func)


    def funcBotaoClear(self):
        self.mostrador.setText('')
    

    def funcEvalIgual(self):
        try:
            sentenca = []
            sentenca.append(self.mostrador.text())
            print(sentenca)
            resultado = [e.lstrip('0') for e in sentenca]
            print(resultado[0])
            self.mostrador.setText(
                str(eval(str(resultado[0])))
            )
        except Exception:
            self.mostrador.setText(
                'Operação Inválida'
            )
    

    def funcSQRT(self):
        try:
            self.mostrador.setText(
                str(math.sqrt(float(self.mostrador.text())))
            )
        except Exception:
            self.mostrador.setText(
                'Operação Inválida'
            )
    

    def setBotoes(self):
        self.componentesBotoes(QPushButton('C', self), 1, 0, 1, 1, self.funcBotaoClear)
        self.componentesBotoes(QPushButton('**', self), 1, 1, 1, 1)
        self.componentesBotoes(QPushButton('SQRT', self), 1, 2, 1, 1, self.funcSQRT)
        self.componentesBotoes(QPushButton('*', self), 1, 3, 1, 1)
        self.componentesBotoes(QPushButton('9', self), 2, 0, 1, 1)
        self.componentesBotoes(QPushButton('8', self), 2, 1, 1, 1)
        self.componentesBotoes(QPushButton('7', self), 2, 2, 1, 1)
        self.componentesBotoes(QPushButton('/', self), 2, 3, 1, 1)
        self.componentesBotoes(QPushButton('6', self), 3, 0, 1, 1)
        self.componentesBotoes(QPushButton('5', self), 3, 1, 1, 1)
        self.componentesBotoes(QPushButton('4', self), 3, 2, 1, 1)
        self.componentesBotoes(QPushButton('+', self), 3, 3, 1, 1)
        self.componentesBotoes(QPushButton('3', self), 4, 0, 1, 1)
        self.componentesBotoes(QPushButton('2', self), 4, 1, 1, 1)
        self.componentesBotoes(QPushButton('1', self), 4, 2, 1, 1)
        self.componentesBotoes(QPushButton('-', self), 4, 3, 1, 1)
        self.componentesBotoes(QPushButton('0', self), 5, 0, 1, 1)
        self.componentesBotoes(QPushButton('.', self), 5, 1, 1, 1)
        self.componentesBotoes(QPushButton('=', self), 5, 2, 1, 2, self.funcEvalIgual)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()
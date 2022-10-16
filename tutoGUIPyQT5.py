from sqlite3 import connect
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout


class App(QMainWindow):
    def __init__(self, parent=None)-> None:
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.btn = QPushButton('Click')
        self.btn.clicked.connect(self.action)
        self.grid.addWidget(self.btn, 0, 0, 1, 1)
        self.setCentralWidget(self.cw)

    def action(self):
        print('Aqui tem coragem!!!')



if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()

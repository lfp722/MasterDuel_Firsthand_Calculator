import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QLineEdit, QMessageBox, QLabel
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import pyqtSlot


# calculate
def cal(deck, need, first):
    if first: # going first
        i = 1
        odds = (deck - need) / deck
        while i < 5:
            odds = odds * ((deck - need - i) / (deck - i))
            print('a')
            i += 1
        return 1 - round(odds, 2)

    elif not first:
        i = 1
        odds = (deck - need) / deck
        while i < 6:
            odds = odds * ((deck - need - i) / (deck - i))
            print('a')
            i += 1
        return 1 - round(odds, 2)


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Simple FirstHand Calculator'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create deck textbox
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(20, 40)
        self.textbox1.resize(280, 40)

        # Create Hand textbox
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(20, 120)
        self.textbox2.resize(280, 40)


        # Create a button in the window
        self.button = QPushButton('Calculate', self)
        self.button.move(20, 160)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        deck = self.textbox1.text()
        hand = self.textbox2.text()
        odd = cal(int(deck), int(hand), True)
        QMessageBox.question(self, 'odds:', str(odd))


app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec())

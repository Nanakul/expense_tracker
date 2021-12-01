from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.label = QtWidgets.QLabel(self)
        self.weekly_expense_button = QtWidgets.QPushButton(self)
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Expense Tracker')
        self.initialize_ui()

    def initialize_ui(self):
        self.label.setText('Not clicked.')
        self.label.move(50, 50)

        self.weekly_expense_button.setText('Weekly Expenses')
        self.weekly_expense_button.setGeometry(0, 0, 130, 50)
        self.weekly_expense_button.clicked.connect(self.weekly_expense_button_click)

    def weekly_expense_button_click(self):
        self.label.setText('You have clicked the button!')
        self.update()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()
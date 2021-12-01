from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize
from expense_tracker import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setGeometry(450, 300, 500, 300)
        self.setWindowTitle('Expense Tracker')
        self.all_expenses_button()

    def all_expenses_button(self):
        self.all_exp_button = QPushButton('All Expenses', self)
        self.all_exp_button.setText('All Expenses')
        self.all_exp_button.setGeometry(0, 0, 130, 50)
        self.all_exp_button.clicked.connect(self.all_exp_button_click)

    def all_exp_button_click(self):
        display_all_expenses()
        self.update()


def window():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


window()
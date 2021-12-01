from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton
from all_expense_window import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # Set MainWindow size and title.
        self.setGeometry(450, 300, 500, 300)
        self.setWindowTitle('Expense Tracker')
        self.all_expenses_button()

    def all_expenses_button(self):
        self.all_exp_button = QPushButton('All Expenses', self)
        self.all_exp_button.setGeometry(25, 25, 130, 50)
        self.all_exp_button.clicked.connect(self.all_exp_button_click)

    def all_exp_button_click(self):
        self.all_exp_window()
        self.win1 = QtWidgets.QMainWindow()
        self.all_exp_ui = AllExpenseWindow()
        self.all_exp_ui.all_exp_setup(self.win1)
        self.all_exp_ui.show_all_exp()
        self.win1.show()

    def all_exp_window(self):
        self.aew = AllExpenseWindow()

def window():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


window()
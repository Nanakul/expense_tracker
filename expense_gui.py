from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QPushButton
from all_expense_window import *
from to_current_window import *
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # Set MainWindow size and title.
        self.setGeometry(450, 300, 300, 300)
        self.setWindowTitle('Expense Tracker')
        self.all_expenses_button()
        self.to_current_exp_button()

    # All Expense Button
    def all_expenses_button(self):
        self.all_exp_button = QPushButton('All Expenses', self)
        self.all_exp_button.setGeometry(5, 25, 150, 50)
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

    # All Expenses to Current
    def to_current_exp_button(self):
        self.to_current_button = QPushButton('Expenses to Current', self)
        self.to_current_button.setGeometry(145, 25, 150, 50)
        self.to_current_button.clicked.connect(self.to_current_button_click)

    def to_current_button_click(self):
        self.to_current_window()
        self.win2 = QtWidgets.QMainWindow()
        self.to_current_exp_ui = ToCurrentWindow()
        self.to_current_exp_ui.to_current_exp_setup(self.win2)
        self.to_current_exp_ui.show_to_current_exp()
        self.win2.show()

    def to_current_window(self):
        self.tce = ToCurrentWindow()

def window():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


window()
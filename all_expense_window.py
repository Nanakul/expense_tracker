from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets, QtCore, QtGui
from expense_tracker import *


class AllExpenseWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def all_exp_setup(self, window1):
        window1.setObjectName('all_exp_window')
        window1.resize(200, 200)
        self.centralwidget = QtWidgets.QWidget(window1)
        self.setWindowTitle('All Expenses')
        self.centralwidget.setObjectName('centralwidget')
        window1.setCentralWidget(self.centralwidget)

        self.all_exp_results = QtWidgets.QGroupBox('All Expenses', self.centralwidget)
        self.all_exp_output = QtWidgets.QTextBrowser(self.all_exp_results)
        self.all_exp_output.setGeometry(0, 0, 200, 200)
        self.all_exp_output.setObjectName('all_exp_output')

        self.retranslate_ui(window1)
        QtCore.QMetaObject.connectSlotsByName(window1)

    def retranslate_ui(self, window1):
        _translate = QtCore.QCoreApplication.translate
        window1.setWindowTitle(_translate('window1', 'All Expenses'))

    def show_all_exp(self):
        self.all_exp_output.append(str(display_all_expenses()))

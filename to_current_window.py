from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWidgets, QtCore
from expense_tracker import *

class ToCurrentWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def to_current_exp_setup(self, window2):
        window2.setObjectName('to_current_exp_window')
        window2.resize(200, 200)
        self.centralwidget = QtWidgets.QWidget(window2)
        self.setWindowTitle('To Current Expenses')
        self.centralwidget.setObjectName('centralwidget')
        window2.setCentralWidget(self.centralwidget)

        self.to_current_exp_results = QtWidgets.QGroupBox('To Current Expenses', self.centralwidget)
        self.to_current_exp_output = QtWidgets.QTextBrowser(self.to_current_exp_results)
        self.to_current_exp_output.setGeometry(0, 0, 200, 200)
        self.to_current_exp_output.setObjectName('all_exp_output')

        self.retranslate_ui(window2)
        QtCore.QMetaObject.connectSlotsByName(window2)

    def retranslate_ui(self, window2):
        _translate = QtCore.QCoreApplication.translate
        window2.setWindowTitle(_translate('window2', 'To Current Expenses'))

    def show_to_current_exp(self):
        self.to_current_exp_output.append(str(display_expense_to_current()))
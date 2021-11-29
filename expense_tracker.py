import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from datetime import datetime
import sqlite3 as db
import pandas as pd
import sys


# Connect the database
# connect = db.connect('MyExpenses.sqlite')
# cursor = connect.cursor()
# cursor.execute("""CREATE TABLE Expenses (
#                 item VARCHAR,
#                 date VARCHAR,
#                 price VARCHAR
#                 )""")
# connect.commit()


# 1.) Display Date and Time
# 2.) Ask user for what they bought
# 3.) Ask user what day they bought it
# 4.) Ask how much it cost
# 5.) Save info to database


def new_expense():
    item = input('What did you purchase? ')
    date_purchased = input('What day did you make the purchase? Format: MM/DD/YYYY ')
    item_price = float(input('How much did this cost? '))

    # connect.execute('INSERT INTO Expenses VALUES (:item, :date, :price)',
    #                 (str({item}), str({date_purchased}), str({item_price})))
    # connect.commit()
    # print(cursor.fetchall())
    # connect.commit()
    # connect.close()


new_expense()


# class MyWindow(QMainWindow):
#     def __init__(self):
#         super(MyWindow, self).__init__()
#         self.label = QtWidgets.QLabel(self)
#         self.weekly_expense_button = QtWidgets.QPushButton(self)
#         self.setGeometry(300, 300, 300, 300)
#         self.setWindowTitle('Expense Tracker')
#         self.initialize_ui()
#
#     def initialize_ui(self):
#         self.label.setText('Not clicked.')
#         self.label.move(50, 50)
#
#         self.weekly_expense_button.setText('Weekly Expenses')
#         self.weekly_expense_button.setGeometry(0, 0, 130, 50)
#         self.weekly_expense_button.clicked.connect(self.weekly_expense_button_click)
#
#     def weekly_expense_button_click(self):
#         self.label.setText('You have clicked the button!')
#         self.update()
#
#     def update(self):
#         self.label.adjustSize()


# def window():
#     app = QApplication(sys.argv)
#     win = MyWindow()
#     win.show()
#     sys.exit(app.exec_())


# window()

if __name__ == '__main__':
    pass

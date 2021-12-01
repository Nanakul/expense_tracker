import sqlite3 as db
import re

# 1 -- Entering expenses == DONE
# 2 -- Return all expenses == DONE
# 3 -- Return all expenses from current date to specified date == DONE
# 4 -- Return all expenses between two specified dates == DONE

# Connect the database
connection = db.connect('Expenses.db')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE if NOT EXISTS Expenses (
                item VARCHAR, 
                date datetime, 
                price VARCHAR
                )""")
connection.commit()


def new_expense():
    """This function will allow a user to input a new expense."""
    while True:
        item = input('What did you purchase? ')
        date_purchased = input('What day did you make the purchase? Format: MM/DD/YYYY ')
        item_price = input('How much did this cost? ')
        d1_format = re.search(r'\d{2}/\d{2}/\d{4}', date_purchased)

        if d1_format is None:
            print('Please re-enter using the instructed format.')
        else:
            break

    connection.execute('INSERT INTO Expenses VALUES (?, ?, ?)',
                       (str(item), str(date_purchased), str(item_price)))
    connection.commit()


def display_all_expenses():
    """This function will display all expenses."""
    cursor.execute('SELECT * FROM Expenses')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    connection.commit()

    return rows


def display_expense_to_current():
    """This function will display all expenses up until the current date (day on which function was run)."""
    cursor.execute('SELECT strftime("%m/%d/%Y", "now")')
    cursor.execute('SELECT * FROM Expenses WHERE date < strftime("%m/%d/%Y", "now")'
                   'ORDER BY date')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    connection.commit()

    return rows


def expense_between_range():
    """This function will allow a user to specify a range of dates to gather expense information."""
    # Correct Format Variable
    while True:
        date1 = input('Enter a date to get expense range from. Format: MM/DD/YYYY ')
        date2 = input('Enter the end date. Format: MM/DD/YYYY ')
        d1_format = re.search(r'\d{2}/\d{2}/\d{4}', date1)
        d2_format = re.search(r'\d{2}/\d{2}/\d{4}', date2)
        if d1_format is None or d2_format is None:
            print('Please re-enter using the instructed format.')
        else:
            break

    cursor.execute('SELECT strftime("%m/%d/%Y", "now")')
    cursor.execute('SELECT * FROM Expenses WHERE date BETWEEN (?) and (?)', (str(date1), str(date2)))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    connection.commit()


if __name__ == '__main__':
    # new_expense()
    # display_all_expenses()
    display_expense_to_current()
    # expense_between_range()

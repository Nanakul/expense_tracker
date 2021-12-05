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
                category VARCHAR,
                item VARCHAR, 
                date datetime, 
                price VARCHAR
                )""")
connection.commit()


def get_category():
    """This function will allow the user to enter the category of what they purchased."""
    while True:
        category = input('What category does your purchase fall under? '
                         '\n (1) == Travel'
                         '\n (2) == Food'
                         '\n (3) == Groceries ')
        try:
            category = int(category)
            if category in range(1, 4):
                break
            else:
                print('Please enter one of the valid categories')
        except ValueError:
            print('Please enter one of the options')
            continue

    return category


def get_item():
    """This function will allow the user to enter in the item they purchased."""
    while True:
        item = input('What did you purchase? ')
        if len(item) != 0:
            return item
        else:
            print('You must have bought something... Try again.')


def get_date_purchased():
    """This function will allow the user to enter in the date of the purchase."""
    while True:
        date_purchased = input('What day did you make the purchase? Format: YYYY/MM/DD ')
        d1_format = re.search(r'\d{4}/\d{2}/\d{2}', date_purchased)

        if d1_format is None:
            print('Please re-enter using the instructed format.')
        else:
            return date_purchased


def get_price():
    while True:
        item_price = input('How much did this cost? $')
        try:
            item_price = float(item_price)
            return str(item_price)
        except ValueError:
            print('Please enter with the following format: #.#')


def input_expense_database(_category, _item, _date_purchased, _price):
    cursor.execute('INSERT INTO Expenses VALUES (?,?,?,?)',
                   (str(_category), str(_item), str(_date_purchased), str(_price)))
    connection.commit()


def display_all_expenses():
    """This function will display all expenses."""
    cursor.execute('SELECT * FROM Expenses ORDER BY date')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    connection.commit()

    return rows


def display_expense_to_current():
    """This function will display all expenses up until the current date (day on which function was run)."""
    cursor.execute('SELECT strftime("%Y/%m/%d", "now")')
    cursor.execute('SELECT * FROM Expenses WHERE date < strftime("%Y/%m/%d", "now")'
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
        date1 = input('Enter a date to get expense range from. Format: YYYY/MM/DD ')
        date2 = input('Enter the end date. Format: YYYY/MM/DD ')
        d1_format = re.search(r'\d{4}/\d{2}/\d{2}', date1)
        d2_format = re.search(r'\d{4}/\d{2}/\d{2}', date2)
        if d1_format is None or d2_format is None:
            print('Please re-enter using the instructed format.')
        else:
            break

    cursor.execute('SELECT strftime("%Y/%m/%d", "now")')
    cursor.execute('SELECT * FROM Expenses WHERE date BETWEEN (?) and (?)', (str(date1), str(date2)))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    connection.commit()


def calc_category_percentages():
    travel_count = 0
    food_count = 0
    groceries_count = 0

    cursor.execute('SELECT COUNT(*) FROM EXPENSES')
    total_expenses = cursor.fetchall()
    print(total_expenses[0][0])

    cursor.execute('SELECT category FROM Expenses')
    category_select = cursor.fetchall()
    
    for category_num in category_select:
        print(category_num[0])


if __name__ == '__main__':
    # category = get_category()
    # item = get_item()
    # date_purchased = get_date_purchased()
    # price = get_price()
    # input_expense_database(category, item, date_purchased, price)
    calc_category_percentages()
    # display_all_expenses()
    # display_expense_to_current()
    # expense_between_range()

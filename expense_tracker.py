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
            if category in range(1, 3):
                break
            else:
                print('Please enter one of the valid categories')
        except ValueError:
            print('Please enter one of the options')
            continue

    return category


def input_expense_database(category, item, date_purchased, price):
    """This function will input the expense into the DB."""

    category = get_category()
    item = get_item()
    date_purchased = get_date_purchased()
    price = get_price()

    # Get Price

    # Insert into DB
    tableName = 'Expense'
    insertIntoTable(tableName, category, itemName, purchaseDate, price)

    connection.execute('INSERT INTO Expenses VALUES (?, ?, ?, ?)',
                       (str(category), str(item), str(date_purchased), str(item_price)))
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


if __name__ == '__main__':
    new_expense()
    # display_all_expenses()
    # display_expense_to_current()
    # expense_between_range()

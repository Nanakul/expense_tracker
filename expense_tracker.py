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


def calc_total_dollars_spent():
    total_dollars_spent = 0.0

    # Get $ Amount for each Expense
    cursor.execute('SELECT price FROM Expenses')
    price_select = cursor.fetchall()

    for x in price_select:
        for y in x:
            float_price = float(y)
            total_dollars_spent += float_price

    print(f'You have spent ${total_dollars_spent} out of all expenses recorded.')

    return total_dollars_spent


def calc_travel_percent(total_dollars_spent):
    travel_count = 0
    travel_dollars_spent = 0

    # Get number of travel expenses
    cursor.execute('SELECT COUNT (*) FROM Expenses WHERE category ="1"')
    total_travel_exp = cursor.fetchall()
    total_travel_exp_int = int(total_travel_exp[0][0])

    cursor.execute('SELECT category FROM Expenses')
    travel_select = cursor.fetchall()

    for x in travel_select:
        for y in x:
            if y == '1':
                travel_count += 1
            else:
                pass

    # Get $ percent spent on travel.
    cursor.execute('SELECT price FROM Expenses WHERE category ="1"')
    travel_prices = cursor.fetchall()

    for i in travel_prices:
        for j in i:
            float_travel_price = float(j)
            travel_dollars_spent += float_travel_price
            
    print(f'You have {total_travel_exp_int} Travel expense(s) recorded.')
    print(f'Out of ${total_dollars_spent} spent, you have spent ${travel_dollars_spent} in the Travel category.')


def calc_category_percentages():
    travel_count = 0
    food_count = 0
    groceries_count = 0

    # Get Total Number of Expenses.
    cursor.execute('SELECT COUNT(*) FROM Expenses')
    total_expenses = cursor.fetchall()
    total_expenses_int = int(total_expenses[0][0])

    print(f'There have been {total_expenses_int} total expenses recorded.')

    cursor.execute('SELECT category FROM Expenses')
    category_select = cursor.fetchall()

    for x in category_select:
        for y in x:
            if y == '1':
                travel_count += 1
            elif y == '2':
                food_count += 1
            else:
                groceries_count += 1

    # Make new table for categories so we can replace this if statement later and do this all on DB level.

    travel_percentage = '%.2f' % (travel_count / total_expenses_int)
    food_percentage = '%.2f' % (food_count / total_expenses_int)
    groceries_percentage = '%.2f' % (groceries_count / total_expenses_int)

    print(f'{travel_percentage}% of your expenses were spent on Travel.')
    print(f'{food_percentage}% of your expenses were spent on Food.')
    print(f'{groceries_percentage}% of your expenses were spent on Groceries.')

    # NOTE: '%.2f' % _____ is to make float precision 2 places to the right.
    return travel_percentage, food_percentage, groceries_percentage


if __name__ == '__main__':
    # category = get_category()
    # item = get_item()
    # date_purchased = get_date_purchased()
    # price = get_price()
    total_dollars_spent = calc_total_dollars_spent()
    # input_expense_database(category, item, date_purchased, price)
    # calc_total_dollars_spent()
    calc_travel_percent(total_dollars_spent)
    # calc_category_percentages()
    # display_all_expenses()
    # display_expense_to_current()
    # expense_between_range()

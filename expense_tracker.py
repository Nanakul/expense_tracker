import sqlite3 as db
import re
from datetime import datetime

# 1 -- Entering expenses == DONE
# 2 -- Return all expenses == DONE
# 3 -- Return all expenses from current date to specified date == DONE
# 4 -- Return all expenses between two specified dates == DONE

# Date and time
date_now = datetime.now().date().strftime('%m-%d-%Y')
time_now = datetime.now().strftime('%I:%M:%S %p')

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


def get_total_num_expenses():

    # Get Total Number of Expenses.
    cursor.execute('SELECT COUNT(*) FROM Expenses')
    total_expenses = cursor.fetchall()
    total_expenses_int = int(total_expenses[0][0])

    return total_expenses_int


def calc_total_dollars_spent():
    total_dollars_spent = 0

    # Get $ Amount for each Expense
    cursor.execute('SELECT price FROM Expenses')
    price_select = cursor.fetchall()

    for x in price_select:
        for y in x:
            float_price = float(y)
            total_dollars_spent += float_price

    return '%.2f' % total_dollars_spent


def calc_travel_percent(_total_num_expenses, _total_dollars_spent):
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

    # Get percentage out of all expenses.
    total_travel_perc = '%.2f' % (total_travel_exp_int / total_num_expenses)

    print(f'You have {total_travel_exp_int} Travel expense(s) recorded out of {total_num_expenses} total expenses.')
    print(f'Out of ${total_dollars_spent} spent:\nYou have spent ${travel_dollars_spent}'
          f'({total_travel_perc}%) in the Travel category.')
    print('-----------------------------------------------------------------------------')

    return travel_dollars_spent, total_travel_perc


def calc_food_percent(_total_num_expenses, _total_dollars_spent):
    food_count = 0
    food_dollars_spent = 0

    # Get number of food expenses
    cursor.execute('SELECT COUNT (*) FROM Expenses WHERE category ="2"')
    total_food_exp = cursor.fetchall()
    total_food_exp_int = int(total_food_exp[0][0])

    cursor.execute('SELECT category FROM Expenses')
    food_select = cursor.fetchall()

    for x in food_select:
        for y in x:
            if y == '2':
                food_count += 1
            else:
                pass

    # Get $ percent spent on food.
    cursor.execute('SELECT price FROM Expenses WHERE category ="2"')
    food_prices = cursor.fetchall()

    for i in food_prices:
        for j in i:
            float_food_price = float(j)
            food_dollars_spent += float_food_price

    # Get percentage out of all expenses.
    total_food_perc = '%.2f' % (total_food_exp_int / total_num_expenses)

    print(f'You have {total_food_exp_int} Food expense(s) recorded out of {total_num_expenses} total expenses.')
    print(f'Out of ${total_dollars_spent} spent:\nYou have spent ${food_dollars_spent}'
          f'({total_food_perc}%) in the Food category.')
    print('-----------------------------------------------------------------------------')

    return food_dollars_spent, total_food_perc


def calc_groceries_percent(_total_num_expenses, _total_dollars_spent):
    groceries_count = 0
    groceries_dollars_spent = 0

    # Get number of groceries expenses
    cursor.execute('SELECT COUNT (*) FROM Expenses WHERE category ="3"')
    total_groceries_exp = cursor.fetchall()
    total_groceries_exp_int = int(total_groceries_exp[0][0])

    cursor.execute('SELECT category FROM Expenses')
    groceries_select = cursor.fetchall()

    for x in groceries_select:
        for y in x:
            if y == '3':
                groceries_count += 1
            else:
                pass

    # Get $ percent spent on groceries.
    cursor.execute('SELECT price FROM Expenses WHERE category ="3"')
    groceries_prices = cursor.fetchall()

    for i in groceries_prices:
        for j in i:
            float_groceries_price = float(j)
            groceries_dollars_spent += float_groceries_price

    # Get percentage out of all expenses.
    total_groceries_perc = '%.2f' % (total_groceries_exp_int / total_num_expenses)

    print(f'You have {total_groceries_exp_int} Groceries expense(s) recorded out of {total_num_expenses} total expenses.')
    print(f'Out of ${total_dollars_spent} spent:\nYou have spent ${groceries_dollars_spent}'
          f'({total_groceries_perc}%) in the Groceries category.')
    print('-----------------------------------------------------------------------------')

    return groceries_dollars_spent, total_groceries_perc


if __name__ == '__main__':
    # category = get_category()
    # item = get_item()
    # date_purchased = get_date_purchased()
    # price = get_price()
    # input_expense_database(category, item, date_purchased, price)
    total_dollars_spent = calc_total_dollars_spent()
    total_num_expenses = get_total_num_expenses()
    # calc_total_dollars_spent()
    # calc_travel_percent(total_num_expenses, total_dollars_spent)
    # calc_food_percent(total_num_expenses, total_dollars_spent)
    # calc_groceries_percent(total_num_expenses, total_dollars_spent)
    # display_all_expenses()
    # display_expense_to_current()
    # expense_between_range()

    exit_program = False

    print('++++++++++++++++++++++++++++++')
    print('-----------WELCOME!-----------')
    print('DATE: ' + date_now)
    print('TIME: ' + time_now)
    print('++++++++++++++++++++++++++++++\n')

    while not exit_program:
        choose_option = int(input('What would you like to do?\n'
                                  '1.) Enter in a new expense.\n'
                                  '2.) Display all expenses to current.\n'
                                  '3.) Get expenses between a particular time frame.\n'
                                  '4.) See spending summary.\n'
                                  '5.) Exit\n'
                                  'Choose 1-5.\n'))

        if choose_option == 1:
            category = get_category()
            item = get_item()
            date_purchased = get_date_purchased()
            price = get_price()
            input_expense_database(category, item, date_purchased, price)
        elif choose_option == 2:
            display_expense_to_current()
            print('\n-----------------------------------------------------------------------------\n')
        elif choose_option == 3:
            expense_between_range()
            print('\n-----------------------------------------------------------------------------\n')
        elif choose_option == 4:
            category_selected = False
            print('What category did you want to see your stats on?\n'
                  '1.) Travel\n'
                  '2.) Food\n'
                  '3.) Groceries\n'
                  '4.) All\n'
                  '5.) Go back')

            while not category_selected:
                user_select_category = int(input('Please enter your option. 1-5.\n'))

                if user_select_category == 1:
                    calc_travel_percent(total_num_expenses, total_dollars_spent)
                elif user_select_category == 2:
                    calc_food_percent(total_num_expenses, total_dollars_spent)
                elif user_select_category == 3:
                    calc_groceries_percent(total_num_expenses, total_dollars_spent)
                elif user_select_category == 4:
                    calc_travel_percent(total_num_expenses, total_dollars_spent)
                    calc_food_percent(total_num_expenses, total_dollars_spent)
                    calc_groceries_percent(total_num_expenses, total_dollars_spent)
                elif user_select_category == 5:
                    break
                else:
                    print('Sorry, please enter a valid option.')

        elif choose_option == 5:
            break
        else:
            print('Sorry, please enter a valid option.')

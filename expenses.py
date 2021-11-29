from datetime import datetime

# 1.) Display Date and Time
# 2.) Ask user for what they bought
# 3.) Ask user what day they bought it
# 4.) Ask how much it cost
# 5.) Save info to database

date_now = datetime.now().date().strftime('%m-%d-%Y')
time_now = datetime.now().strftime('%I:%M:%S %p')
expense_list = []


def welcome():
    exit_program = False

    print('++++++++++++++++++++++++++++++')
    print('-----------WELCOME!-----------')
    print('DATE: ' + date_now)
    print('TIME: ' + time_now)
    print('++++++++++++++++++++++++++++++')
    print('1.) Enter in a new expense. \n2.) Check your weekly expenses. '
          '\n3.) Check your monthly expenses. \n4.) Exit.')

    while not exit_program:
        choose_option = int(input('What would you like to do? 1-4 \n'))

        if choose_option == 1:
            new_expense()
        elif choose_option == 2:
            print(expense_list)
        elif choose_option == 3:
            print(expense_list)
        elif choose_option == 4:
            exit_program = True
        else:
            print('Sorry, please enter a valid option.')


def new_expense():
    item = input('What did you buy? ')
    date_purchased = input('What day did you make this purchase? Format: MM/DD/YYYY ')
    item_price = float(input('How much did it cost? '))
    expense_list.append([item, date_purchased, item_price])


if __name__ == '__main__':
    welcome()

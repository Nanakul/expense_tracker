from datetime import datetime

# 1.) Display Date and Time
# 2.) Ask user for what they bought
# 3.) Ask user what day they bought it
# 4.) Ask how much it cost
# 5.) Save info to database

date_now = datetime.now().date().strftime('%m-%d-%Y')
time_now = datetime.now().strftime('%I:%M:%S %p')


def welcome():
    print('++++++++++++++++++++++++++++++')
    print('-----------WELCOME!-----------')
    print('DATE: ' + date_now)
    print('TIME: ' + time_now)
    print('++++++++++++++++++++++++++++++')
    choose_option = input('What would you like to do? ')


if __name__ == '__main__':
    welcome()

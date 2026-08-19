from db_connection import *
from series import *

init_tables()

loggined_in_user = None

while True:
    choice = input('[1] - Register User\n[2] - Login\n[3] - Get Profile\n[0] - Exit\nChoice: ')
    match choice:
        case '1':
            print('=====REGISTER FORM=====')
            username,password,email = input('Username: '),input('Password: '),input('Email: ')
            register(username,password,email)
        case '2':
            print('=====LOGINED FROM=====')
            username,password = input('Username: '),input('Password: ')
            user = login(username,password)
            if user:
                loggined_in_user = user
                print(f'\nWelcome, {user[1]}\n')
                while loggined_in_user:
                    choice = input('=====TASK MENU=====\n[1] - Add Task\n[2] - Get Task By ID\n[3] - Show Task\n[4] - Complete Task\n[5] - Update Task\n[6] - Delete Task\n[0] - Log Out\nChoice: ')
                    match choice:
                        case '0':
                            loggined_in_user = None
                        case _:
                            print('Choice: Another Option')
        case '3':
            if loggined_in_user:
                print(f'ID: {loggined_in_user[0]} | USERNAME: {loggined_in_user[1]} | EMAIL: {loggined_in_user[3]}')
            else:
                print('User Not Loggined')
        case '0':
            print('You EXIT')
            break
        case _:
            print('Invalid Input')
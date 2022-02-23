import os

import psycopg2
import pyperclip
from prettytable import PrettyTable
from psycopg2 import Error

from authenticate import authenticate
from randomPasswordGenerator import checker


def establish_conn_server(query, description, fetch_data):
    try:
        connection = psycopg2.connect(user="postgres", password="A@2008viral",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="passm")

        cursor = connection.cursor()

        query = query
        descrip = description
        print(descrip + '...')

        cursor.execute(query)
        connection.commit()

        if fetch_data == True:
            data = cursor.fetchall()
            return data
        elif fetch_data == False:
            pass
        else:
            print("Wrong Input In Data Fetch...")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while creating PostgreSQL table", error)

    finally:
        # Closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            # print("PostgreSQL connection is closed")


def start():
    # List Of Provided Functions
    global l
    l = ['View Exisitng Service Password',
         'Add New Account (Service)', 'Remove Account (Service)', 'List All Registered Services', 'See Serviices By E-Mail']
    print("List Of Functions You Can Perform  :")
    for i in range(len(l)):
        print(f"{i}. {l[i]}")
    inp = int(
        input("Enter Serial Number Of The Function You Want To Perform : "))
    os.system("clear")
    print(f'The Action(s) You Want To Perform Is - {inp}')
    print()

    if (inp == 0):    # View Exisitng Service Password
        status_repeat = True
        while (status_repeat == True):
            os.system("clear")
            service = str(input(
                "What Service's Info Do You Want To View (Press '\q' to exit from search)? "))
            if service == "\q" or service == "\Q":
                status_repeat = False
                break
            else:
                v = establish_conn_server(
                    f'''SELECT * FROM accounts WHERE service LIKE '%{service}%';''', 'Checking If Service Exists', True)
                if (v == []):
                    print()
                    print("Error... Entered Service Does Not Exist")
                    print("Please Try Again")
                else:
                    if (len(v) == 1):
                        pyperclip.copy(v[0][2])
                    else:
                        print(
                            'There Are Multiple Enteries For This Service(s) As Listed...')

                    try:
                        print(v)
                        print(type(v))
                        print()
                        l = v
                        table = PrettyTable(['Service', 'Email', 'Password'])
                        for rec in l:
                            table.add_row(rec)
                        print(table)
                    except KeyboardInterrupt:
                        print('[+] Exiting...')
                        os.system("exit")
                        os.system("exit")

                    # for i in range(len(v)):
                    #     # print(v)
                    #     print()
                    #     print(f'Service: {v[i][0]}')
                    #     print(f'Email: {v[i][1]}')
                    #     print(f'Password: {v[i][2]}')
                    #     if i > 5:
                    #         print()
                    #         print('More...')
                    #         break
            inp = input("")
            if inp == "" or inp == " ":  # So That It Waits & Doesn't Clear Result
                pass
            else:
                pass
    elif (inp == 1):  # Add New Account
        service = str(input("What Service Do You Want To Add? "))
        email = str(input("What Email Do You Want To Add? "))
        password = checker()
        pyperclip.copy(password)

        query_add_row = f'''INSERT INTO accounts (service,email,password) VALUES ('{service}', '{email}', '{password}'); '''

        v = establish_conn_server(query_add_row, 'Row Added', False)
    elif (inp == 2):  # Remove An Account
        service = str(input("What Service Do You Want To Remove? "))
        query_check_row = f'''SELECT * FROM accounts WHERE service='{service}';'''
        v = establish_conn_server(
            query_check_row, 'Checking If Service Exists', True)
        if not v == []:
            query_remove_row = f'''DELETE FROM accounts WHERE service = '{service}';'''
            v = establish_conn_server(query_remove_row, 'Row Removed', False)
        else:
            print()
            print("Error... Entered Service Does Not Exist")
            print("Please Try Again")
    elif (inp == 3):  # List All Registered Services
        query_get_allRows = f'''SELECT * FROM accounts'''
        v = establish_conn_server(
            query_get_allRows, 'Getting All Services', True)
        print(v)
        print()
        print()

        l = v

        table = PrettyTable(['Service', 'Email', 'Password'])

        for rec in l:
            table.add_row(rec)

        print(table)
        # show_limit = 3
        # for i in range(len(v)):
        #     if (i > show_limit):
        #         print(
        #             "More... Follow The Instructions TO View Full List")
        #         break
        #     # print(v)
        #     print()
        #     print(f'Service: {v[i][0]}')
        #     print(f'Email: {v[i][1]}')
        #     print(f'Password: {v[i][2]}')
        # print()
        # print("To View Your Data In A Table Format, DO The Following : ")
        # print("1. sudo -u postgres psql passm (copied to clipboard)")
        # print("2. Enter Sudo Password")
        # print("3. select * from accounts;")
    elif (inp == 4):  # See Serviices By E-Mail
        email = str(input("What Email's Services Do You Want To View? "))
        v = establish_conn_server(
            f'''select * from accounts where email='{email}';''', 'Fteching Services', True)
        print(f'Email: {email}')
        print()

        l = v
        table = PrettyTable(['Service', 'Email', 'Password'])
        for rec in l:
            table.add_row(rec)
        print(table)

        # for i in range(len(v)):
        #     service = v[i][0]
        #     password = v[i][2]

        #     print()
        #     print(f'Service {i}: {service}')
        #     print(f'Password {i}: {password}')

        # print(v)
        # print(type(v))
    else:             # Error For Inputting Invalid Number
        os.system("clear")
        print("Wrong Input... Please Try Again")
        start()


def funcAuth(go_ahead):
    if go_ahead == True:
        auth = authenticate()
        if auth == True:
            start()
        elif auth == False:
            pass
    else:
        os.system("clear")
        print("Couldnt Start... System Error !")
        os.system("exit")  # ZSH (Root)
        os.system("exit")  # Root (Base Env)
        os.system("exit")  # Terminal


funcAuth(True)


# print(l)

# def try1():
#     try:
#         global l
#         l = []  # All Services
#         service = str(input("What Service Do You Want To Add?"))
#         password = str(input("What Paasword Do You Want To Add?"))
#         d = {service: password}
#         l.append(d)
#         print("Password Added")
#     except:
#         print("Error IN Inputting Data... Please Try Again")
#         try1()

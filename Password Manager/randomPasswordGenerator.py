import os
import random as rd
import string

# def checker():
#     print()
#     print('A) Generate New Automatic Secure Password')
#     print('B) Enter Your Own Password')
#     inp1 = str(input("Answer : "))

#     if (inp1 == 'A' or inp1 == 'a'):
#         password = generator()
#         print('The Password Is' + password)
#     elif (inp1 == 'B' or inp1 == 'b'):
#         password = str(input(
#             "What Paasword Do You Want To Add? "))
#         print(password)
#     else:
#         print("Error... Wrong Input")
#         os.system("exit")
#         password = False
#     return password


def checker():
    inp1 = str(input(
        "What Paasword Do You Want To Add (If You Leave Blank, Then Random Password WIll Be Inserted)? "))
    print()
    # print('A) Generate New Automatic Secure Password')
    # print('B) Enter Your Own Password')
    # inp1 = str(input("Answer : "))

    if (inp1 == '' or inp1 == ' '):
        password = generator()
        print('The New Secure (Auto-Generated) Password Is' + password)
    else:
        password = inp1
    return password


def generator():
    # prompt = "Plese Enter, Number Of Keys In Password : "
    # numOfKeys = int(input(prompt))
    numOfKeys = 10
    password = []
    for i in range(numOfKeys):
        n = rd.randint(1, 2)
        if n == 1:
            v = rd.choice(string.ascii_letters)
            password.append(v)
        elif n == 2:
            v = rd.randint(0, 9)
            password.append(v)
        else:
            print("Some Error In Program...")
    print('New Password (Copied To Clipboard) : ')
    new_password = ' '.join([str(elem) for elem in password])
    new_password = new_password.replace(" ", "")
    print(new_password)
    return new_password

    # for i in range(numOfKeys):
    #     print(password[i], end='')

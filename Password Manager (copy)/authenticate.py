import getpass
import os


def authenticate():
    f = open("mpass.txt", 'r')
    v = f.readline()
    v = v[:-1]
    masterpassword = v
    inp_verify = getpass.getpass("Please Enter Master Password : ")

    global status

    if inp_verify == masterpassword:
        status = True
    else:
        status = False
        # os.system("clear")
        print("Wrong Password !!")
        exiting = input("Press Enter To Exit")
        if exiting == "" or " ":
            os.system("exit")
    return status

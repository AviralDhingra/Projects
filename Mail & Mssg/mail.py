# This Module Support Gmail & Microsoft Accounts (hotmail, outlook etc..)
import os
import random as rd
import string

from mailer import Mailer


def email_send():
    print("This Module Support Gmail & Microsoft Accounts (hotmail, outlook etc..")
    email_inp = input("Email : ")
    subject_inp = input("Subject : ")
    mssg_inp = input("Message : ")

    mail = Mailer(email='aviral270608@gmail.com', password='A@2008viral')
    mail.send(receiver=email_inp,
              subject=subject_inp, message=mssg_inp)


def email_verify(receiver, software_name, number0fKeys):
    # Creating A Code
    numOfKeys = number0fKeys
    code = []
    for i in range(numOfKeys):
        n = rd.randint(1, 2)
        if n == 1:
            v = rd.choice(string.ascii_letters)
            code.append(v)
        elif n == 2:
            v = rd.randint(0, 9)
            code.append(v)
        else:
            print("Some Error In Program...")
    code = ' '.join([str(elem) for elem in code])
    code = code.replace(" ", "")

    # Standard Mssg
    mssg = f'Your Verification Code is : {code}\nThis Is A temprorary Security Key, Please Use It With Care'
    # Establishing Connection & Sending Email
    mail = Mailer(email='aviral270608@gmail.com', password='A@2008viral')
    mail.send(receiver=receiver,
              subject=f'Verification For {software_name}', message=mssg)

    # Verification
    inp = input("Code : ")
    if inp == code:
        print("Verfied !!")
        status_verification = True
    else:
        print("Wrong Code...")
        os.system("exit")
        status_verification = False
    return status_verification


authenticate = email_verify('ambika.handa@gmail.com', 'Microsoft Store', 7)
print(authenticate)

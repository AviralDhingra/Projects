import os

from functions_compile import *
from functions_compile import basicFunctionality

# class basicActions():
#     def error(se):
#         os.system("clear")
#         print(se)
#         print("Error... Please Try Again")
#         print()
#         start()

#     def endMsg():
#         print("Process Successfully Excuted...")
#         print()
#         print("Thank You For Using This Program, Exiting...")
#         os.system("exit")

#     def askPath(actionName):
#         try:
#             global path
#             path = str(
#                 input(f"Please Enter Folder Path, In Which You Want To {actionName} : "))
#             os.chdir(path)
#             return path
#             # print(path)
#         except FileNotFoundError:
#             print("Wrong Folder Path... Please Try Again")
#             start()


def start():
    # List Of Function That You Can Perform
    l = ["Exit", "Delete Files By Type", "Move Files BY Type"]
    try:
        print("What Do You Want To Perform In This Folder ?")
        print("Options (Type The Number) : ")
        for i in range(len(l)):
            print(f"{i}. {l[i]}")
        functionToUse = int(input(""))
    except:
        basicActions.error("Function Error !!")

    if functionToUse == 0:
        print("Exiting...")
        os.system("exit")
        os.system("clear")
        os.system("clear")  # To Make Sure No Error Shows
        print("Exiting...")
    elif functionToUse == 1:
        print("These Are Some Pre-made Functions : ")
        print("1. Delete Unecessary Files In Downloads Folder")
        print("2. Delete All Zip Type Files In A Folder")
        global inp_delete_files
        inp_delete_files = str(input(
            "Press Enter If You Want To Continue With Custom Delete Or The Number Of The Pre-built Function... "))
        if inp_delete_files == "" or inp_delete_files == " ":
            status = True
        else:
            status = False
        basicFunctionality.deleteFilesByType(status)
        basicActions.endMsg()
    elif functionToUse == 2:
        inp = str(input("Which Type Do You Want To Move ?"))
        inp2 = str(input("What Path DO You Want To Move The File(s) To ?"))
        basicFunctionality.moveFilesByType(inp, inp2)
        basicActions.endMsg()

    else:
        basicActions.error(
            f"{functionToUse} Is A Wrong Input, The Function Number Doent Exist...")


start()
os.system("exit")

import os

# from terminal_ui import start


class basicActions():
    def error(se):
        os.system("exit")
        os.system("clear")
        print(se)
        print("Error... Please Try Again")
        print()
        os.chdir(r'/home/deathblade287/Dropbox/Projects/File Manager')
        os.system("python3 terminal_ui.py")

    def endMsg():
        print("Process Successfully Excuted...")
        print()
        print("Thank You For Using This Program, Exiting...")
        os.system("python3 terminal_ui.py")

    def askPath(actionName):
        try:
            global path
            path = str(
                input(f"Please Enter Folder Path, In Which You Want To {actionName} : "))
            os.chdir(path)
            return path
            # print(path)
        except FileNotFoundError:
            print("Wrong Folder Path... Please Try Again")
            os.system("python3 terminal_ui.py")

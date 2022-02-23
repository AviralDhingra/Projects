import glob
import os

from basicActions import basicActions


class basicFunctionality():
    def deleteFilesByType(status, number):
        inp_delete_files = number
        status = status
        if status == True:
            path = basicActions.askPath("Delete From")
            os.chdir(path)
            fileType = str(input("Which File Type DO You Want To Delete ?"))
            filesSelected = glob.glob(f'*{fileType}')
            for i in range(len(filesSelected)):
                if os.path.exists(filesSelected[i]):
                    os.remove(filesSelected[i])
                else:
                    basicActions.error(
                        f"File Number {i} ({filesSelected[i]}) Do Not Exist")
            if not filesSelected == []:
                print("Deleting Files : ")
                print(filesSelected)
                basicActions.endMsg()
            else:
                basicActions.error(
                    f"No Files Of Type '{fileType}' Exist In The Directory Chosen.")
        elif status == False:
            functionNum = inp_delete_files
            functionNum = int(functionNum)
            if functionNum == 1:  # Delete Unecessary Files In Downloads Folder
                print("Deleting Unecessary Files...")
                print(
                    " File Types : .exe, .deb, .appimage, .run, .ova, etc Will Be Deleted From The Downloads Folder")
                inp = input("Are You Sure You Want To Continue ?")
                os.chdir(r'/home/deathblade287/Downloads')
                l = ['.exe', '.deb', '.appimage', '.run', '.ova']
                print("Deleting Files : ")
                for i in range(len(l)):
                    fileType = l[i]
                    filesSelected = glob.glob(f'*{fileType}')
                    print(filesSelected)
                basicActions.endMsg()

            elif functionNum == 2:  # Delete All Zip Type Files In A Folder
                path = basicActions.askPath("Perform This Function")
                os.chdir(path)
                l = ['.zip', '.tar', '.gz', '.7z']

                print("Deleting Unecessary Files...")
                print(
                    f"File Types {l} : Will Be Deleted From Provided Paths")
                inp = input("Are You Sure You Want To Continue ?")

                print("Deleting Files : ")
                for i in range(len(l)):
                    fileType = l[i]
                    filesSelected = glob.glob(f'*{fileType}')
                    print(filesSelected)
                basicActions.endMsg()
            else:
                basicActions.error(
                    f"PreBuilt Function Number - {functionNum} Doesnt Exist")

    def moveFilesByType(fileType, movePath):
        # TODO Add pre-built functions in this to... a) move all os type files to documents folder assigned
        path = basicActions.askPath("move files")
        filesSelected = glob.glob(f'*{fileType}')
        print(filesSelected)
        for i in range(len(filesSelected)):
            if os.path.exists(filesSelected[i]):
                os.rename(f'{path}/{filesSelected[i]}',
                          f'{movePath}/{filesSelected[i]}')
            else:
                basicActions.error(
                    f"File(s) Number {i} ({filesSelected[i]}) Does Not Exist")


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
        os.system("exit")
        os.system("clear")
    elif functionToUse == 1:
        print("These Are Some Pre-made Functions : ")
        print("1. Delete Unecessary Files In Downloads Folder")
        print("2. Delete All Zip Type Files In A Folder")
        inp_delete_files = str(input(
            "Press Enter If You Want To Continue With Custom Delete Or The Number Of The Pre-built Function... "))
        if inp_delete_files == "" or inp_delete_files == " ":
            status = True
        else:
            status = False
        # print(inp_delete_files)
        # print(status)
        basicFunctionality.deleteFilesByType(status, inp_delete_files)
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

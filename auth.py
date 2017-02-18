#!data-env/bin/python3
import pygsheets
import sys


valid = {"yes": True, "y": True, "ye": True,
         "no": False, "n": False}


def yes_no_prompt(prompt):
    while True:
        sys.stdout.write(prompt)
        choice = input().lower()
        if choice in valid:
            break
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")
    return choice


def main():

    gc = pygsheets.authorize(
        outh_file="client_secret.json",
        outh_nonlocal=True)

    choice = yes_no_prompt("Do you want to create a new sheet? [y/n] ")
    sheet_name = new_sheet(choice)
    if sheet_name is not None:
        gc.create(sheet_name)
    else:
        while True:
            sys.stdout.write("Name of Google Sheet: ")
            sheet_name = input().lower()
            if sheet_name != "" and sheet_name in gc.list_ssheets():
                break
            elif sheet_name not in gc.list_ssheets():
                choice = yes_no_prompt(
                    "That sheet does not exist. Try creating a new one? [y/n] ")
                if valid[choice]:
                    sheet_name = new_sheet(choice)
                    gc.create(sheet_name)
                    break
            else:
                sys.stdout.write(
                    "Please respond with the name of the Google Sheet.\n")

    sh = gc.open(sheet_name)
    wks = sh.sheet1
    wks.update_cell("A1", "test")


def new_sheet(choice):
    if valid[choice]:
        while True:
            sys.stdout.write("Name of Google Sheet: ")
            choice = input().lower()
            if choice != "":
                break
            else:
                sys.stdout.write(
                    "Please respond with a name for the Google Sheet.\n")
        return choice
    else:
        return None


if __name__ == "__main__":
    main()

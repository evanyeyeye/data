#!data-env/bin/python3
import pygsheets
import sys


def main():

    gc = pygsheets.authorize(outh_file="client_secret.json", outh_nonlocal=True)
    
    new = new_sheet()
    if new != None:
        gc.create(new)
    
    sh = gc.open("a test sheet")
    wks = sh.sheet1
    wks.update_cell("A1", "test")

def new_sheet():
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    
    while True:
        sys.stdout.write("Do you want to create a new sheet? [y/n] ")
        choice = input().lower()
        if choice in valid:
            break;
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")
    
    if valid[choice]:
        while True:
            sys.stdout.write("Name of Google Sheet: ")
            choice = input().lower()
            if choice != "":
                break;
            else:
                sys.stdout.write("Please respond with a name for the Google Sheet.\n")
        return choice;
    else:
        return None;

if __name__ == "__main__":
    main()

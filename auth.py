#!data-env/bin/python3
import pygsheets

gc = pygsheets.authorize(outh_file="client_secret.json", outh_nonlocal=True)

sh = gc.open("a test sheet")
wks = sh.sheet1
wks.update_cell("A1", "test")


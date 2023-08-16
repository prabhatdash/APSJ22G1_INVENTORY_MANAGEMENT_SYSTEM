import mysql.connector as mc
try:
    dbc = mc.connect(host="localhost", user="akshat", passwd="rootakshat", database="inventory")
    cursor = dbc.cursor()
except Exception as e:
    print(e)
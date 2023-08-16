import time
import auth
import pandas as pd
import connector as con
def login():
    a = ("ENTER THE USER ID TO LOGIN: ")
    user_id = input(a)
    fetch_query = "select * from registration_details;"
    con.cursor.execute(fetch_query)
    count = 0
    for i in con.cursor:
        if user_id == i[2]:
            count = count + 1
            print("                                                 Please wait we are sending the OTP to the given ID........")
            login_stat = auth.auth(user_id)
    if count == 0:
        print("                                                                  USER NOT REGISTERED !")
        print("                                 +---------------------------------------------------------------------------------+")
        print("                                 |                              Do you Want to Register?                           |")
        print("                                 | Type YES to Register                                            Type NO to exit |")
        print("                                 +---------------------------------------------------------------------------------+")
        reg = input()
        reg2 = reg.upper()
        if reg2 == "NO":
            print("Thank You")
            exit()
        elif reg2 == "YES":
            registration()
    return user_id

def registration():
    print("+-----------------------------------------------------+")
    name=("     ENTER YOUR NAME: ")
    un=input(name)
    email=("     ENTER EMAIL ID: ")
    ue=input(email)
    print("+-----------------------------------------------------+")
    query="insert into registration_details (name,email) values" +"('"+un+"','"+ue+"');"
    con.cursor.execute(query)
    con.dbc.commit()
    print("                      ******************************************* REGISTRATION COMPLETED ! ********************************************")
    login()
    menu()

def view_items():
    fetch_query = "select * from product_table;"
    con.cursor.execute(fetch_query)
    data=[]
    for i in con.cursor:
        data.append(i)
    df=pd.DataFrame(data,columns=['S.No.','Product_ID','Product_Name','Cat_ID','Brand','Price','Purchase_Date'])
    print(df.to_markdown(index=False))
    print("                                 +------------------------------------------------------------------------------------------+")
    print("                                 |                              Do you Want to go to Menu Again?                            |")
    print("                                 | Type y to go Back                                                         Type n to exit |")
    print("                                 +------------------------------------------------------------------------------------------+")
    rm2 = ("ENTER YOUR CHOICE:")
    rm = (input(rm2))
    if rm == "y":
        menu()
    elif rm == "n":
        print("Thank You")
        exit()

def cat_quantity():
    fetch_query = "select category_table.cat_id,category_table.items,count(*) as quantity from category_table,product_table where product_table.cat_id=category_table.cat_id group by cat_id;"
    con.cursor.execute(fetch_query)
    data=[]
    for i in con.cursor:
        data.append(i)
    df=pd.DataFrame(data,columns=['Cat_Id','Items','Quantity'])
    print(df.to_markdown(index=False))
    print("                                 +------------------------------------------------------------------------------------------+")
    print("                                 |                              Do you Want to go to Menu Again?                            |")
    print("                                 | Type y to go Back                                                         Type n to exit |")
    print("                                 +------------------------------------------------------------------------------------------+")
    rm2 = ("ENTER YOUR CHOICE:")
    rm = (input(rm2))
    if rm == "y":
        menu()
    elif rm == "n":
        print("Thank You")
        exit()

def delete_record():
    fetch_query = "select * from product_table;"
    con.cursor.execute(fetch_query)
    data=[]
    for i in con.cursor:
        data.append(i)
    df=pd.DataFrame(data,columns=['S.No.','Product_ID','Product_Name','Cat_ID','Brand','Price','Purchase_Date'])
    print(df.to_markdown(index=False))
    print("Enter the S.No of Product you want to delete")
    s_no=int(input())
    insert_query="insert into deleted_records select * from product_table where s_no="+str(s_no)+";"
    con.cursor.execute(insert_query)
    con.dbc.commit()
    delete_query="delete from product_table where s_no="+str(s_no)+";"
    con.cursor.execute(delete_query)
    con.dbc.commit()
    fetch_query = "select * from product_table;"
    con.cursor.execute(fetch_query)
    data = []
    for i in con.cursor:
        data.append(i)
    df = pd.DataFrame(data,
                      columns=['S.No.', 'Product_ID', 'Product_Name', 'Cat_ID', 'Brand', 'Price', 'Purchase_Date'])
    print(df.to_markdown(index=False))
    print("******************************************* DELETED SUCCESSFULLY ! ********************************************")
    print("                                 +------------------------------------------------------------------------------------------+")
    print("                                 |                              Do you Want to go to Menu Again?                            |")
    print("                                 | Type y to go Back                                                         Type n to exit |")
    print("                                 +------------------------------------------------------------------------------------------+")
    rm2 = ("ENTER YOUR CHOICE:")
    rm = (input(rm2))
    if rm == "y":
        menu()
    elif rm == "n":
        print("Thank You")
        exit()

def update_sno():
    fetch_query = "select * from product_table;"
    con.cursor.execute(fetch_query)
    data = []
    for i in con.cursor:
        data.append(i)
    df = pd.DataFrame(data, columns=['S.No.', 'Product_ID', 'Product_Name', 'Cat_ID', 'Brand', 'Price', 'Purchase_Date'])
    print(df.to_markdown(index=False))
    print("Enter the Old S_no: ")
    old = input()
    print("Enter the New S_no: ")
    vlu = input()
    update_query = "update product_table set s_no = "+vlu+" where s_no="+old+";"
    con.cursor.execute(update_query)
    con.dbc.commit()
    data = []
    for i in con.cursor:
        data.append(i)
    fetch_query = "select * from product_table;"
    con.cursor.execute(fetch_query)
    data = []
    for i in con.cursor:
        data.append(i)
    df = pd.DataFrame(data,
                      columns=['S.No.', 'Product_ID', 'Product_Name', 'Cat_ID', 'Brand', 'Price', 'Purchase_Date'])
    print(df.to_markdown(index=False))
    print("******************************************* UPDATED SUCCESSFULLY ! ********************************************")
    print("                                 +------------------------------------------------------------------------------------------+")
    print("                                 |                              Do you Want to go to Menu Again?                            |")
    print("                                 | Type y to go Back                                                         Type n to exit |")
    print("                                 +------------------------------------------------------------------------------------------+")
    rm2 = ("ENTER YOUR CHOICE:")
    rm = (input(rm2))
    if rm == "y":
        menu()
    elif rm == "n":
        print("Thank You")
        exit()

def price():
    fetch_query = "select * from product_table;"
    con.cursor.execute(fetch_query)
    data = []
    for i in con.cursor:
        data.append(i)
    df = pd.DataFrame(data,
                      columns=['S.No.', 'Product_ID', 'Product_Name', 'Cat_ID', 'Brand', 'Price', 'Purchase_Date'])
    print(df.to_markdown(index=False))
    print("Enter the S_No of product: ")
    sno = input()
    print("Enter the New Price: ")
    vlu = input()
    update_query = "update product_table set price = "+vlu+" where s_no="+sno+";"
    con.cursor.execute(update_query)
    con.dbc.commit()
    data = []
    for i in con.cursor:
        data.append(i)
    fetch_query = "select * from product_table;"
    con.cursor.execute(fetch_query)
    data = []
    for i in con.cursor:
        data.append(i)
    df = pd.DataFrame(data, columns=['S.No.', 'Product_ID', 'Product_Name', 'Cat_ID', 'Brand', 'Price', 'Purchase_Date'])
    print(df.to_markdown(index=False))
    print("******************************************* UPDATED SUCCESSFULLY ! ********************************************")
    print("                                 +------------------------------------------------------------------------------------------+")
    print("                                 |                              Do you Want to go to Menu Again?                            |")
    print("                                 | Type y to go Back                                                         Type n to exit |")
    print("                                 +------------------------------------------------------------------------------------------+")
    rm2 = ("ENTER YOUR CHOICE:")
    rm = (input(rm2))
    if rm == "y":
        menu()
    elif rm == "n":
        print("Thank You")
        exit()

def product_id():
    s= "select * from product_table;"
    con.cursor.execute(s)
    data = []
    for i in con.cursor:
        data.append(i)
    df = pd.DataFrame(data,
                      columns=['S.No.', 'Product_ID', 'Product_Name', 'Cat_ID', 'Brand', 'Price', 'Purchase_Date'])
    print(df.to_markdown(index=False))
    print("Enter the S_no of Product_ID whose value you want to Update: ")
    sno= input()
    print("Enter the new Product_ID")
    new= input()
    product_query="update product_table set product_id = " + "'" +new+ "' where s_no="  +sno+";"
    con.cursor.execute(product_query)
    con.dbc.commit()
    con.cursor.execute("select * from product_table;")
    data = []
    for i in con.cursor:
        data.append(i)
    df = pd.DataFrame(data, columns=['S.No.', 'Product_ID', 'Product_Name', 'Cat_ID', 'Brand', 'Price', 'Purchase_Date'])
    print(df.to_markdown(index=False))
    print("******************************************* UPDATED SUCCESSFULLY ! ********************************************")
    print("                                 +------------------------------------------------------------------------------------------+")
    print("                                 |                              Do you Want to go to Menu Again?                            |")
    print("                                 | Type y to go Back                                                         Type n to exit |")
    print("                                 +------------------------------------------------------------------------------------------+")
    rm2 = ("ENTER YOUR CHOICE:")
    rm = (input(rm2))
    if rm == "y":
        menu()
    elif rm == "n":
        print("Thank You")
        exit()

def product_name():
    name_query = "select * from product_table;"
    con.cursor.execute(name_query)
    data = []
    for i in con.cursor:
        data.append(i)
    df = pd.DataFrame(data,
                          columns=['S.No.', 'Product_ID', 'Product_Name', 'Cat_ID', 'Brand', 'Price', 'Purchase_Date'])
    print(df.to_markdown(index=False))
    print("Enter the S_no of Product_Name whose value you want to Update: ")
    sno = input()
    print("Enter the new Product_Name")
    new = input()
    name_query = "update product_table set product_name = " + "'" + new + "' where s_no=" + sno + ";"
    con.cursor.execute(name_query)
    con.dbc.commit()
    con.cursor.execute("select * from product_table;")
    data = []
    for i in con.cursor:
        data.append(i)
    df = pd.DataFrame(data,
                          columns=['S.No.', 'Product_ID', 'Product_Name', 'Cat_ID', 'Brand', 'Price', 'Purchase_Date'])
    print(df.to_markdown(index=False))
    print("******************************************* UPDATED SUCCESSFULLY ! ********************************************")
    print("                                 +------------------------------------------------------------------------------------------+")
    print("                                 |                              Do you Want to go to Menu Again?                            |")
    print("                                 | Type y to go Back                                                         Type n to exit |")
    print("                                 +------------------------------------------------------------------------------------------+")
    rm2 = ("ENTER YOUR CHOICE:")
    rm = (input(rm2))
    if rm == "y":
        menu()
    elif rm == "n":
        print("Thank You")
        exit()

def cat_ID():
    cat_query = "select * from product_table;"
    con.cursor.execute(cat_query)
    data = []
    for i in con.cursor:
        data.append(i)
    df = pd.DataFrame(data,
                          columns=['S.No.', 'Product_ID', 'Product_Name', 'Cat_ID', 'Brand', 'Price', 'Purchase_Date'])
    print(df.to_markdown(index=False))
    print("Enter the S_no of cat_ID whose value you want to Update: ")
    sno = input()
    print("Enter the new cat_ID")
    new = input()
    cat_query = "update product_table set cat_ID = " + "'" + new + "' where s_no=" + sno + ";"
    con.cursor.execute(cat_query)
    con.dbc.commit()
    con.cursor.execute("select * from product_table;")
    data = []
    for i in con.cursor:
        data.append(i)
    df = pd.DataFrame(data,
                          columns=['S.No.', 'Product_ID', 'Product_Name', 'Cat_ID', 'Brand', 'Price', 'Purchase_Date'])
    print(df.to_markdown(index=False))
    print("******************************************* UPDATED SUCCESSFULLY ! ********************************************")
    print("                                 +------------------------------------------------------------------------------------------+")
    print("                                 |                              Do you Want to go to Menu Again?                            |")
    print("                                 | Type y to go Back                                                         Type n to exit |")
    print("                                 +------------------------------------------------------------------------------------------+")
    rm2 = ("ENTER YOUR CHOICE:")
    rm = (input(rm2))
    if rm == "y":
        menu()
    elif rm == "n":
        print("Thank You")
        exit()
def insert():
    brand_query = "select * from product_table;"
    con.cursor.execute(brand_query)
    data = []
    for i in con.cursor:
        data.append(i)
    df = pd.DataFrame(data, columns=['S.No.', 'Product_ID', 'Product_Name', 'Cat_ID', 'Brand', 'Price', 'Purchase_Date'])
    print(df.to_markdown(index=False))
    print("Enter the S_no of New Product")
    s=input()
    print("Enter the Product_id of New Product")
    id=input()
    print("Enter the Product_Name of New Product")
    pn=input()
    print("Enter the Cat_ID of New_Product")
    cid=input()
    print("Enter the Brand of New_Product")
    bnd=input()
    print("Enter the Price of New_Product")
    prc=input()
    print("Enter the Purchase_date of New_Product in format (yyyy-mm-dd)")
    npd=input()
    insert_query = "insert into product_table values(" +s+ ",""'" +id+ "'"",""'" +pn+ "'"",""'" +cid+ "'"",""'" +bnd+ "'""," +prc+ "," "'" +npd+ "'"");"
    con.cursor.execute(insert_query)
    con.dbc.commit()
    con.cursor.execute("select * from product_table;")
    data=[]
    for i in con.cursor:
        data.append(i)
    df = pd.DataFrame(data, columns=['S.No.', 'Product_ID', 'Product_Name', 'Cat_ID', 'Brand', 'Price', 'Purchase_Date'])
    print(df.to_markdown(index=False))
    print("****************************************** ITEM INSERTED SUCCESSFULLY ! ******************************************")
    print("                                 +------------------------------------------------------------------------------------------+")
    print("                                 |                              Do you Want to go to Menu Again?                            |")
    print("                                 | Type y to go Back                                                         Type n to exit |")
    print("                                 +------------------------------------------------------------------------------------------+")
    rm2 = ("ENTER YOUR CHOICE:")
    rm = (input(rm2))
    if rm == "y":
        menu()
    elif rm == "n":
        print("Thank You")
        exit()

def brand():
    brand_query = "select * from product_table;"
    con.cursor.execute(brand_query)
    data = []
    for i in con.cursor:
        data.append(i)
    df = pd.DataFrame(data, columns=['S.No.', 'Product_ID', 'Product_Name', 'Cat_ID', 'Brand', 'Price', 'Purchase_Date'])
    print(df.to_markdown(index=False))
    print("Enter the S_no of Brand whose value you want to Update: ")
    sno = input()
    print("Enter the new Brand Name")
    new = input()
    bra_query = "update product_table set Brand = " + "'" + new + "' where s_no=" + sno + ";"
    con.cursor.execute(bra_query)
    con.dbc.commit()
    con.cursor.execute("select * from product_table;")
    data = []
    for i in con.cursor:
        data.append(i)
    df = pd.DataFrame(data,
                          columns=['S.No.', 'Product_ID', 'Product_Name', 'Cat_ID', 'Brand', 'Price', 'Purchase_Date'])
    print(df.to_markdown(index=False))
    print("******************************************* UPDATED SUCCESSFULLY ! ********************************************")
    print("                                 +------------------------------------------------------------------------------------------+")
    print("                                 |                              Do you Want to go to Menu Again?                            |")
    print("                                 | Type y to go Back                                                         Type n to exit |")
    print("                                 +------------------------------------------------------------------------------------------+")
    rm2 = ("ENTER YOUR CHOICE:")
    rm = (input(rm2))
    if rm == "y":
        menu()
    elif rm == "n":
        print("Thank You")
        exit()

def date():
    date_query = "select * from product_table;"
    con.cursor.execute(date_query)
    data = []
    for i in con.cursor:
        data.append(i)
    df = pd.DataFrame(data,columns=['S.No.', 'Product_ID', 'Product_Name', 'Cat_ID', 'Brand', 'Price', 'Purchase_Date'])
    print(df.to_markdown(index=False))
    print("Enter the S_no of Purchase_Date whose value you want to Update: ")
    sno = input()
    print("Enter New Day")
    dd=input()
    print("Enter New Month")
    mm=input()
    print("Enter New Year")
    yyyy=input()
    new_date=yyyy+"-"+mm+"-"+dd
    date_query = "update product_table set purchase_date = " + "'"+new_date+"' where s_no=" + sno + ";"
    con.cursor.execute(date_query)
    con.dbc.commit()
    con.cursor.execute("select * from product_table;")
    data = []
    for i in con.cursor:
        data.append(i)
    df = pd.DataFrame(data, columns=['S.No.', 'Product_ID', 'Product_Name', 'Cat_ID', 'Brand', 'Price', 'Purchase_Date'])
    print(df.to_markdown(index=False))
    print("******************************************* UPDATED SUCCESSFULLY ! ********************************************")
    print("                                 +------------------------------------------------------------------------------------------+")
    print("                                 |                              Do you Want to go to Menu Again?                            |")
    print("                                 | Type y to go Back                                                         Type n to exit |")
    print("                                 +------------------------------------------------------------------------------------------+")
    rm2 = ("ENTER YOUR CHOICE:")
    rm = (input(rm2))
    if rm=="y":
        menu()
    elif rm =="n":
        print("Thank You")
        exit()


def menu():
    print("                                                           +-----------------------------------------+")
    print("                                                           | > Press a to View All Products          |")
    print("                                                           | > Press b to See Category Wise Quantity |")
    print("                                                           | > Press c to Delete Record              |")
    print("                                                           | > Press d to Update S_no                |")
    print("                                                           | > Press e to Update Product_id          |")
    print("                                                           | > Press f to Update Product_name        |")
    print("                                                           | > Press g to Update Cat_id              |")
    print("                                                           | > Press h to Update Brand               |")
    print("                                                           | > Press i to Update Price               |")
    print("                                                           | > Press j to Update Purchase_date       |")
    print("                                                           | > Press k to Insert New Product         |")
    print("                                                           | > Type logout to end                    |")
    print("                                                           +-----------------------------------------+")
    b = ("Enter your Choice: ")
    user_input = (input(b))
    if user_input == "a":
        view_items()
    elif user_input == "b":
        cat_quantity()
    elif user_input == "c":
        delete_record()
    elif user_input == "d":
        update_sno()
    elif user_input == "e":
        product_id()
    elif user_input == "f":
        product_name()
    elif user_input == "g":
        cat_ID()
    elif user_input == "h":
        brand()
    elif user_input == "i":
        price()
    elif user_input == "j":
        date()
    elif user_input == "k":
        insert()
    elif user_input == "logout":
        logout()

def logout():
    print("                                 +------------------------------------------------------------------------------------------+")
    print("                                 |                                   Do you Want to LOGOUT?                                 |")
    print("                                 |            Yes                                                               No          |")
    print("                                 +------------------------------------------------------------------------------------------+")
    lo2 = ("ENTER YOUR CHOICE:")
    lo = (input(lo2))
    if lo == "Yes":
        print("                                                             Please Wait, Logging Out...")
        time.sleep(2)
        print("                             ************************************* LOGOUT SUCCESSFULL ! *********************************")
        time.sleep(2)
        login()


class Format:
    end = '\033[0m'
    underline = '\033[4m'

print("                                               +---------------------------------------------------+")
print("                                               |  ",Format.underline+"WELCOME TO THE IT INVENTORY MANAGEMENT SYSTEM"+ Format.end,"  |                                                       ")
print("                                               +---------------------------------------------------+")
print("----------------------------------------------------------- SELECT THE OPTION TO BEGIN ! -----------------------------------------------------------------------------------------------------")
print("                                                   +-----------------------------------------+")
print("                                                   |             Press 1 to Login            |")
print("                                                   |            Press 2 to Register          |")
print("                                                   +-----------------------------------------+")
a=("Enter your Choice: ")
user_input=int(input(a))

if user_input==1:
    val=login()
    fetch_query = "select name from registration_details where email='"+val+"';"
    con.cursor.execute(fetch_query)
    name=None
    for i in con.cursor:
        name=i[0]
    name=name.upper()
    if val!=0:
        class Format:
            end = '\033[0m'
            underline = '\033[4m'


        print("                                     +-----------------------------------------------------------------------------------------------+")
        print("                                                        ",Format.underline + "HEY ! "+name+" LOGIN SUCCESSFUL SELECT AN OPTION TO BEGIN" + Format.end,"                    ")
        print("                                     +-----------------------------------------------------------------------------------------------+")
        print("                                                           +-----------------------------------------+")
        print("                                                           | > Press a to view all products          |")
        print("                                                           | > Press b to See Category Wise Quantity |")
        print("                                                           | > Press c to Delete Record              |")
        print("                                                           | > Press d to Update S_no                |")
        print("                                                           | > Press e to Update product_id          |")
        print("                                                           | > Press f to Update product_name        |")
        print("                                                           | > Press g to Update cat_id              |")
        print("                                                           | > Press h to Update brand               |")
        print("                                                           | > Press i to Update price               |")
        print("                                                           | > Press j to Update purchase_date       |")
        print("                                                           | > Press k to Insert New Product         |")
        print("                                                           | > Type logout to end                    |")
        print("                                                           +-----------------------------------------+")
        a = ("Enter your Choice: ")
        user_input = (input(a))
        if user_input == "a":
            view_items()
        elif user_input == "b":
            cat_quantity()
        elif user_input == "c":
            delete_record()
        elif user_input == "d":
            update_sno()
        elif user_input == "e":
            product_id()
        elif user_input == "f":
            product_name()
        elif user_input == "g":
            cat_ID()
        elif user_input == "h":
            brand()
        elif user_input == "i":
            price()
        elif user_input == "j":
            date()
        elif user_input == "k":
            insert()
        elif user_input == "logout":
            logout()
elif user_input == 2:
    registration()

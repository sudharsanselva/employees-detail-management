from tabulate import tabulate
import mysql.connector

con = mysql.connector.connect(host='localhost', username='root', password='Sudhar@12', database='project')

try:
    def insert(Name, Age, Address, City):
        my_cursor = con.cursor()
        sql = "insert into biodata(Name, Age, Address, City) values(%s,%s,%s,%s)"
        user = (Name, Age, Address, City)
        my_cursor.execute(sql,user)
        con.commit()
        print("\n")
        print("DATA INSERTED SUCCESSFULLY....")

    def update(Name, Age, Address, City, ID):
        my_cursor = con.cursor()
        sql = "update  biodata set Name=%s, Age=%s, Address=%s, City=%s where ID=%s"
        user = (Name, Age, Address, City, ID)
        my_cursor.execute(sql,user)
        con.commit()
        print("\n")
        print("DATA UPDATED SUCCESSFULLY....")

    def select():
        my_cursor = con.cursor()
        sql = "select ID, Name, Age, Address, City from biodata "
        my_cursor.execute(sql)
        result = my_cursor.fetchall()
        print(tabulate(result,headers=["ID","NAME","AGE","ADDRESS","CITY"]))
        print("\n")
        print("DATAS ARE EXECUTED SUCCESSFULLY....")
        

    def delete(ID):
        my_cursor = con.cursor()
        sql = "delete from biodata where ID=%s"
        user = (ID,)
        my_cursor.execute(sql,user)
        con.commit()
        print("\n")
        print("DATA DELETED SUCCESSFULLY....")


    while True:
        print("I̲nsert data \n")
        print("U̲pdate data \n")
        print("S̲elect data \n")
        print("D̲elete data \n")
        print("Q̲uit \n")

        choice = input("Enter the First Letter : ")

        if choice in {'i', 'I'}:
            Name = input("Enter the Name: ")
            Age = int(input("Enter the Age: "))
            Address = input("Enter the Address: ")
            City = input("Enter the City: ")
            insert(Name, Age, Address, City)

        elif choice in {'u', 'U'}:
            ID = int(input("Enter the ID : "))
            Name = input("Enter the Name: ")
            Age = int(input("Enter the Age: "))
            Address = input("Enter the Address: ")
            City = input("Enter the City: ")
            update(Name, Age, Address, City,ID)

        elif choice in {'s', 'S'}:
            select()

        elif choice in {'d', 'D'}:
            ID = int(input("Enter the ID: "))
            delete(ID)

        elif choice in {'q', 'Q'}:
            quit()

        else:
            print("PLEASE ENTER THE VALID NUMBER....")

except Exception as e:
    print("error:", e)

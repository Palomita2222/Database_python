import mysql.connector
from bs4 import BeautifulSoup
import os
os.system("cls")

mydb = mysql.connector.connect(
  #If you are not experieced with Python, please only edit the text in the variables between theese comments
  host="localhost",
  user="user",
  password="pass",
  database="Database"
  #If you are not experieced with Python, please only edit the text in the variables between theese comments
)

mycursor = mydb.cursor()

opt = input("Do you want TO APPEND(1), TO READ(2), or TO DELETE(3)? : ")
os.system("cls")
if opt == "1":
    opt2 = input("Do you want to add a TABLE(1) or ADD(2) to current table? : ")
    os.system("cls")
    if opt2 == "1":
        keys = {}
        stri = []
        command = "CREATE TABLE "
        opt3 = input("What name do you want this table to have? :")
        os.system("cls")
        command = command + opt3 + " ("
        opt4 = int(input("How many values do you want the table to have? :"))
        os.system("cls")
        for i in range(opt4):
            keys["value{0}".format(i)] = input("What value do you want the number "+ str(i)+" value to have? : ")
            os.system("cls")
            stri.append(["value{0}".format(i)])
        for i in range(len(stri)):
            command = command + str(stri[i]).replace("'","").replace("[","").replace("]","") + " VARCHAR(255), "
        neatcommand = command[0:-2]
        neatcommand = neatcommand + ")"
        print(neatcommand)
        mycursor.execute(neatcommand)
        print("These are the new tables availiable in the DataBase: ")
        mycursor.execute("SHOW TABLES")
        for i in mycursor:
            print(i)
        input()
        os.system("cls")


    if opt2 == "2":
        print("These are the tables availiable in the DataBase: ")
        mycursor.execute("SHOW TABLES")
        for i in mycursor:
            print(i)
        opt3 = input("Please add the table name here(no spaces & perfect name) : ")
        os.system("cls")
        sql = ("INSERT INTO " + opt3 +" (username,password,platform) VALUES (%s, %s, %s)")
        username = input("Please enter username to store : ")
        os.system("cls")
        password = input("Please enter password to store : ")
        os.system("cls")
        platform = input("Please enter the credentials platform(eg. Youtube) : ")
        os.system("cls")
        usr_data = [username,password,platform]
        mycursor.execute(sql,usr_data)
        mydb.commit()
        mycursor.execute("SELECT * FROM "+opt3)
        myresult = mycursor.fetchall()
        print("")
        for x in myresult:
            print(x)
        input()
        os.system("cls")
        

elif opt == "2":
    print("These are the tables availiable in the DataBase: ")
    mycursor.execute("SHOW TABLES")
    for i in mycursor:
        print(i)
    opt1 = input("Please add the table name here(no spaces & perfect name) : ")
    os.system("cls")
    mycursor.execute("SELECT * FROM "+ opt1)
    data = mycursor.fetchall()
    for i in data:
        print(i)
    if len(data) < 1:
        print("There is no data in this TABLE")
    input()
    os.system("cls")


elif opt == "3":
    command = "DROP TABLE "
    print("These are the tables availiable in the DataBase: ")
    mycursor.execute("SHOW TABLES")
    for i in mycursor:
        print(i)
    opt2 = input("What TABLE do you want to DELETE? : ")
    os.system("cls")
    mycursor.execute(command+opt2)
    print("These are the new tables availiable in the DataBase: ")
    mycursor.execute("SHOW TABLES")
    for i in mycursor:
        print(i)
    input()
    os.system("cls")



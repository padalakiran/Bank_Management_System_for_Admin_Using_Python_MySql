import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=Sql Password,
  database= Name Of DataBase"
    )

mycursor = mydb.cursor()
#function..............................................
def with_dir():
        a=int(input("Enter Account Number: "))
        b=int(input("Enter Phone Number: "))


        sql="SELECT * from customer;"
        mycursor.execute(sql)
        rows=mycursor.fetchall()

        for row in rows:
            if a==row[1]:
                if b==row[2]:
                    c=int(input("Enter Ammount to withDraw: "))
                    sql = """update customer set Amount=Amount-%s where AccountNumber=%s and PhoneNo=%s;"""
                    valus=(c,a,b)
                    mycursor.execute(sql,valus)
                    mydb.commit()
                    print("Hey, {0} You are Sucusfully Debited Ammount..................".format(row[0]))
                else:
                    print("User Not Found ")
         #github:- @padalakiran

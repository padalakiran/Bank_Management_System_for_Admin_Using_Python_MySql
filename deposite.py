import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="kiran1415@A",
  database="PK_Bank"
)

mycursor = mydb.cursor()
#function...................................................
def dep():
    a=int(input("Enter Account Number: "))
    b=int(input("Enter Phone Number: "))


    sql="SELECT * from customer;"
    mycursor.execute(sql)
    rows=mycursor.fetchall()

    for row in rows:
        if a==row[1]:
            if b==row[2]:
                c=int(input("Enter Ammount to Deposite: "))
                sql = """update customer set Amount=Amount+%s where AccountNumber=%s and PhoneNo=%s;"""
                valus=(c,a,b)
                mycursor.execute(sql,valus)
                mydb.commit()
                mydb.close()
                print("Hey, {0} You are Sucusfully Credited Ammount...........".format(row[0]))
                
            else:
                print("User Not Found ")
        
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=Sql Password,
  database= Name Of DataBase"
)

mycursor = mydb.cursor()

def showCu():
 try:
        

        print('what do you want to Show: ')
        print('1.Names','\t','2.Account Numbers',
            '\t','3.Phone Number','\t','4.Ammount','\t'
            ,'5.All Data','\t','6.Specfic Person')
        c=input('enter your choise: ')
        print()
        
        
        ########### Names ################
        if c=='1':
            sql="SELECT Name, AccountNumber from customer;"
            mycursor.execute(sql)
            a = mycursor.fetchall()
            print("Name, AccountNumber")
            for row in a:
                print(row)
            
        ############ Acoount Number ##########
                    
        if c=='2':
            sql="SELECT Name, AccountNumber , Amount from customer;"
            mycursor.execute(sql)
            a = mycursor.fetchall()
            print("Name, AccountNumber , Amount")
            for row in a:
                print(row)
        
        ########### Phone Number #############
        
        if c=='3':
            sql="SELECT name, AccountNumber , PhoneNo from customer;"
            mycursor.execute(sql)
            a = mycursor.fetchall()
            print("Name, AccountNumber , PhoneNo")
            
            for row in a:
                print(row)
        
        ############# Amount ###########
        
        if c=='4':
            sql="SELECT name, AccountNumber ,amount from customer;"
            mycursor.execute(sql)
            a = mycursor.fetchall()
            print("Name, AccountNumber , Amount")
  
            for row in a:
                print(row)
                
        
        ############ All Data #############
        if c=='5':
            sql="SELECT * from customer;"
            mycursor.execute(sql)
            a = mycursor.fetchall()
  
            for row in a:
                print(row)
                print("\n")

            
            
        ########Specific People#########
        
        if c=='6':
            d=int(input("Enter Account Number: "))
            b=int(input("Enter PhoneNumber Number: "))
            sql=" select * from customer where accountnumber =%s and phoneno=%s;"
            values=(d,b)
            mycursor.execute(sql,values)
            a = mycursor.fetchall()
            print()
            for row in a:
                print(row)
                print("\n")


            
 except:
     print("Enter Valid Data")   
#$showCu()

#github:- @padalakiran

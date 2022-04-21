import mysql.connector
import time
import random
import phonenumbers

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="kiran1415@A",
  database="PK_Bank"
)




def create_acc():
    
    print('Whoooo! Your going to be officially our coustomer....')
                #loading animation
    t = 1
    while t < 3:
        print("\rLoading, Please Wait " + ("." * (t*5)), end=" ")
        time.sleep(1)
        t = t + 1
    
    
    print('\n')
    name = input('Enter Name: ')
    AccountNumber=x = random.randint(10000000,999999999)
    print("Your AccountNumber is: {0}".format(AccountNumber))
    amount=int(input('Enter Amount: '))

                
                
    PhoneNo=input('Enter Phone No: ')
    ################ validating Phone number #####################
    
    E1 = phonenumbers.parse("+91"+PhoneNo)
    f=(phonenumbers.is_valid_number(E1))
    
    
    try:         
        if f==True:
                    
            ######################################################################################################################
            ############################################## Adding Data In MySql ##################################################
            ######################################################################################################################
            
            mycursor = mydb.cursor()
    

            sql = """INSERT INTO Customer (Name,AccountNumber, PhoneNo,Amount) VALUES (%s, %s,%s,%s)"""
            val = (name,AccountNumber,PhoneNo,amount)
            mycursor.execute(sql, val)

            mydb.commit()

           # print(mycursor.rowcount, "record inserted.")
        
            print('You are officially Become Our Coustomer......................................')


        else:
            print('Phone Number Is not correct')
    except:
        print("Some Error Occurred")
#create_acc()
import mysql.connector
cur=mysql.connector.connect(host="localhost",user="root",password="varrsan123",database="first2")
csr=cur.cursor()
csr.execute("CREATE table Covid19_Patient_Info(Aadhar_No bigint,Name varchar(50),Test_Result varchar(20) default null,Age int,Phone_No bigint)")
def something():
    while True:
        ask=input("Select any of the three options:\n"
                  "1.E for entering new details\n"
                  "2.U for updating a patients details\n"
                  "3.V for Viewing Details of the test\n"
                  "4.X For Exiting\n"

                  "Type in your answer: ")
        if ask.lower()=="e":
            while True:
                print()
                aadhar=input("Enter the aadhar no of patient: ")
                if len(str(aadhar))==12:
                    if aadhar.isdigit()==True:
                        aadhar=int(aadhar)
                        break
                    else:
                        print("Please enter only digit.")
                else:
                    print("Please enter 12 digits.")
            print()
            name = input("Name of the patient: ")
            while True:
                print()
                age=input("Enter the patient's age: ")
                if age.isdigit()==True:
                    age=int(age)
                    break
                else:
                    print("Please enter only digits.")
            while True:
                print()
                phone_no=input("Enter the patient's phone number: ")
                if phone_no.isdigit()==True:
                    phone_no=int(phone_no)
                    break
                else:
                    print("Please enter only digit.")
            print()
            tresult=input("Enter the test result for the covid test: ")
            print()
            print("The above new details have been updated")
            print()
            csr.execute("INSERT INTO Covid19_Patient_Info(Aadhar_No,name,Test_Result,Age,Phone_No) values(%s,'%s','%s',%s,%s)"%(aadhar,name,tresult,age,phone_no))
            cur.commit()
        elif ask.lower()=="u":
            while True:
                print()
                aadhar=input("Enter the aadhar no of patient: ")
                if len(str(aadhar))==12:
                    if aadhar.isdigit()==True:
                        aadhar=int(aadhar)
                        break
                    else:
                        print("Please enter only digit.")
                else:
                    print("Please enter 12 digits.")
            print()
            name = input("Name of the patient: ")
            while True:
                print()
                age=input("Enter the patient's age: ")
                if age.isdigit()==True:
                    age=int(age)
                    break
                else:
                    print("Please enter only digits.")
            while True:
                print()
                phone_no=input("Enter the patient's phone number: ")
                if phone_no.isdigit()==True:
                    phone_no=int(phone_no)
                    break
            print()
            tresult=input("Enter the test result for the covid test: ")
            print()
            print("The above details have been added")
            print()
            csr.execute("UPDATE Covid19_Patient_Info SET Name='%s',Test_Result='%s',Age=%s,Phone_No=%s WHERE Aadhar_No=%s"%(name,tresult,age,phone_no,aadhar))
            cur.commit()
        elif ask.lower()=="v":
            while True:
                print()
                aadhar=input("Enter your aadhar number: ")
                if len(str(aadhar))==12:
                       if aadhar.isdigit()==True:
                           aadhar=int(aadhar)
                           break
                       else:
                           print("Please enter only digits.")
                else:
                    print("Please enter 12 digits")
            while True:
                csr.execute("SELECT * FROM Covid19_Patient_Info WHERE Aadhar_No=%s"%aadhar)
                result=csr.fetchall()
                print()
                print("The name of the patient is",result[0][1],".")
                print()
                print("The result of the covid test is",result[0][2],".")
                print()
                break
        elif ask.lower()=="x":
            print()
            print("Thankyou!!")
            break
        else:
            print()
            print("Enter only E,U,V or X.")
something()
            
            
        
    
        
    



           

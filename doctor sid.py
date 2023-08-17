import mysql.connector
cur=mysql.connector.connect(host="localhost",user="root",password="varrsan123",database="covid_self6")
csr=cur.cursor()
csr.execute("create table Doctors(Aadhar_No bigint,Name varchar(50),Age int,Gender varchar(50),Phone_No bigint,Patient_Assigned bigint,Speciality varchar(50))")
def doctors():
    while True:
        print()
        ask=input("Select any of the three options:\n"
                  "1.E for entering new details\n"
                  "2.U for updating a doctor's details\n"
                  "3.V for Viewing Details of a doctor\n"
                  "4.X For Exiting\n"

                  "Type in your answer: ")
        if ask.lower()=="e":
            print()
            while True:
                aadhar=input("Enter the aadhar no of doctor: ")
                if len(str(aadhar))==12:
                    if aadhar.isdigit()==True:
                        aadhar=int(aadhar)
                        break
                    else:
                        print("Please enter only digit.")
                else:
                    print("Please enter 12 digits.")
            print()
            name = input("Name of the doctor: ")
            while True:
                print()
                age=input("Age of doctor: ")
                if age.isdigit()==True:
                    age=int(age)
                    break
                else:
                    print("Please enter digits")
            while True:
                print()
                gender=input("Enter the gender of doctor: ")
                if gender.lower()=="male":
                    break
                elif gender.lower()=="female":
                    break
                else:
                    print("Please enter gender as male or female.")        
            while True:
                print()
                phno=input("Phone number of doctor: ")
                if phno.isdigit()==True:
                    phno=int(phno)
                    break
                else:
                    print("Please enter digits")
            while True:
                print()
                ptnt=input("Cid_no of Patient the doctor is assigned to: ")
                if ptnt.isdigit()==True:
                    ptnt=int(ptnt)
                    break
                else:
                    print("Please enter digits")
            print()
            spec=input("Speciality of doctor: ")
            print()
            print("The new details have been added")
            print()
            csr.execute("INSERT INTO Doctors(Aadhar_No,Name,Age,Gender,Phone_No,Patient_Assigned,Speciality) values (%s,'%s',%s,'%s',%s,%s,'%s')"%(aadhar,name,age,gender,phno,ptnt,spec))
            cur.commit()    
        elif ask.lower()=="u":
            while True:
                print()
                aadhar=input("Enter the aadhar no of doctor: ")
                if len(str(aadhar))==12:
                    if aadhar.isdigit()==True:
                        aadhar=int(aadhar)
                        break
                    else:
                        print("Please enter only digit.")
                else:
                    print("Please enter 12 digits.")
            print()
            name=input("Enter the doctor's name: ")
            print()
            while True:
                print()
                age=input("Enter the doctor's age: ")
                if age.isdigit()==True:
                    age=int(age)
                    break
                else:
                    print("Please enter only digits.")
            while True:
                print()
                gender=input("Enter the gender of doctor: ")
                if gender.lower()=="male":
                    break
                elif gender.lower()=="female":
                    break
                else:
                    print("Please enter gender as male or female.")
            while True:
                print()
                phone_no=input("Enter the doctor's phone number: ")
                if phone_no.isdigit()==True:
                    phone_no=int(phone_no)
                    break
                else:
                    print("Please enter only digit.")
            while True:
                print()
                ptnt=input("Cid_no of Patient the doctor is assigned to: ")
                if ptnt.isdigit()==True:
                    ptnt=int(ptnt)
                    break
                else:
                    print("Please enter only digit.")
            print()
            spec=input("Speciality of doctor: ")
            print()
            print("The update is completed.")
            print()
            csr.execute("UPDATE Doctors SET Name='%s',Age=%s,Gender='%s',Phone_No=%s,Patient_Assigned=%s,Speciality='%s' WHERE Aadhar_No=%s"%(name,age,gender,phno,ptnt,spec,aadhar))
            cur.commit()
        elif ask.lower()=="v":
            while True:
                print()
                aadhar=input("Enter the aadhar no of doctor: ")
                if len(str(aadhar))==12:
                    if aadhar.isdigit()==True:
                        aadhar=int(aadhar)
                        break
                    else:
                        print("Please enter only digit.")
                else:
                    print("Please enter 12 digits.")
            while True:
                csr.execute("SELECT * FROM Doctors WHERE Aadhar_No=%s"%aadhar)
                result=csr.fetchall()
                print()
                print("The name of the doctor is",result[0][0],".")
                print()
                print("The age of the doctor is",result[0][1],".")
                print()
                print("The gender of the doctor is",result[0][2],".")
                print()
                print("The phone no of doctor is",result[0][3],".")
                print()
                print("The Cid_no of Patient,the doctor is assigned to is",result[0][4],".")
                print()
                print("The Speciality of the Doctor is",result[0][5],".")
                print()
                break   
        elif ask.lower()=="x":
            print()
            print("Thank You!!")
            break
        else:
            print()
            print("INSERT ONLY E,U,V,X")
doctors()










import mysql.connector
import datetime
import random

t=datetime.datetime.now()
print(t)
print()

cur=mysql.connector.connect(host="localhost",user="root",password="varrsan123",database="project")
csr=cur.cursor()

csr.execute("CREATE table Doctors(Aadhar_No bigint,Name varchar(50),Age int,Gender varchar(50),Phone_No bigint,Patient_Assigned bigint,Speciality varchar(50))")
csr.execute("CREATE table Patients(Aadhar_No BIGINT,Name VARCHAR(20),Age INT,Gender VARCHAR(20),Disease VARCHAR(20),Blood_Group VARCHAR(20),Phone_No BIGINT,Caretaker_Name VARCHAR(20),Caretaker_Phone_No BIGINT,Doctor_Name VARCHAR(20),Food_Types VARCHAR(20))")
csr.execute("CREATE table Authorities(Adhaar_No BIGINT,Beds_Available INT,Beds_Total INT,Oxygen_Cylinders INT,Vaccines_Available INT,Vaccinated INT,Ambulances INT)")
csr.execute("CREATE table Covid19_Details_Info(Unique_ID BIGINT,Confirmed INT,Active INT,Recovered INT,Deceased INT,Vaccinated INT)")
csr.execute("CREATE table Covid19_Patient_Info(Aadhar_No bigint,Name varchar(50),Test_Result varchar(20) default null,Age int,Phone_No bigint)")
cur.commit()

def DocAdd():
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

def DocUpd():
    while True:
        print()
        aadhar=input("Enter the aadhar no of doctor: ")
        int1=csr.execute("Select Count(*) from Doctors where Aadhar_No=%s"%(int(aadhar)))
        if int1!=None:
            if len(str(aadhar))==12:
                if aadhar.isdigit()==True:
                    aadhar=int(aadhar)
                    break
                else:
                    print("Please enter only digit.")
            else:
                print("Please enter 12 digits.")
        else:
            print("The above entered aadhar number is not in our database")  
    print()
    name=input("Enter the doctor's name: ")
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
    csr.execute("UPDATE Doctors SET Name='%s',Age=%s,Gender='%s',Phone_No=%s,Patient_Assigned=%s,Speciality='%s' WHERE Aadhar_No=%s"%(name,age,gender,phone_no,ptnt,spec,aadhar))
    cur.commit() 

def DocView():
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
        print("The name of the doctor is",result[0][1],".")
        print()
        print("The age of the doctor is",result[0][2],".")
        print()
        print("The gender of the doctor is",result[0][3],".")
        print()
        print("The phone no of doctor is",result[0][4],".")
        print()
        print("The Cid_no of Patient,the doctor is assigned to is",result[0][5],".")
        print()
        print("The Speciality of the Doctor is",result[0][6],".")
        print()
        break

def InPatAdd():
    while True:
        print()
        aadhar=input("Enter the aadhar no of inpatient: ")
        if len(str(aadhar))==12:
            if aadhar.isdigit()==True:
                aadhar=int(aadhar)
                break
            else:
                print("Please enter only digit.")
        else:
            print("Please enter 12 digits.")
    print()
    name=input("Enter the patient's name: ")
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
        gender=input("Enter the gender of patient: ")
        if gender.lower()=="male":
            break
        elif gender.lower()=="female":
            break
        else:
            print("Please enter gender as male or female.")
    print()
    disease=input("Enter the disease patient is enduring with: ")
    while True:
        print()
        blood_group=input("""blood group(A+,B+,O+,AB+,A-,B-,O-,AB-):- """)
        if blood_group==("A+") or blood_group==("B+") or blood_group==("O+") or blood_group==("AB+") or blood_group==("A-") or blood_group==("B-") or blood_group==("O-") or blood_group==("AB-"):
            break
        else:
            print("Please enter the below blood group types only.")
    while True:
        print()
        phone_no=input("Enter the patient's phone number: ")
        if phone_no.isdigit()==True:
            phone_no=int(phone_no)
            break
        else:
            print("Please enter only digit.")
    print()
    caretaker_name=input("Enter caretaker name: ")
    while True:
        print()
        caretaker_phone_no=input("Enter caretaker phone no: ")
        if caretaker_phone_no.isdigit()==True:
            caretaker_phone_no=int(caretaker_phone_no)
            break
        else:
            print("Please enter only digit.")
    print()
    doctor_name=input("Enter doctor name: ")
    while True:
        print()
        food_types=input("Enter the food type(veg or nonveg): ")
        if food_types.lower()=="veg":
            break
        elif food_types.lower()=="nonveg":
            break
        else:
            print("Please enter only veg or non veg.")
    print()
    print("The above new details have been added")
    print()
    csr.execute("insert into  Patients(Aadhar_No,Name,Age,Gender,Disease,Blood_Group,Phone_No,Caretaker_Name,Caretaker_Phone_No,Doctor_Name,Food_Types) values(%s,'%s',%s,'%s','%s','%s',%s,'%s',%s,'%s','%s')"%(aadhar,name,age,gender,disease,blood_group,phone_no,caretaker_name,caretaker_phone_no,doctor_name,food_types))
    cur.commit()

def InPatUpd():
    while True:
        print()
        aadhar=input("Enter the aadhar no of inpatient: ")
        int2=csr.execute("Select Count(*) from Patients where Aadhar_No=%s"%(int(aadhar)))
        if int2!=None:
            if len(str(aadhar))==12:
                if aadhar.isdigit()==True:
                    aadhar=int(aadhar)
                    break
                else:
                    print("Please enter only digit.")
            else:
                print("Please enter 12 digits.")
        else:
            print("The above entered entered aadhar number is not in our database")
    print()
    name=input("Enter the patient's name: ")
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
        gender=input("Enter the gender of patient: ")
        if gender.lower()=="male":
            break
        elif gender.lower()=="female":
            break
        else:
            print("Please enter gender as male or female.")
    print()
    disease=input("Enter the disease patient is enduring with: ")
    while True:
        print()
        blood_group=input("""blood group(A+,B+,O+,AB+,A-,B-,O-,AB-):- """)
        if blood_group==("A+") or blood_group==("B+") or blood_group==("O+") or blood_group==("AB+") or blood_group==("A-") or blood_group==("B-") or blood_group==("O-") or blood_group==("AB-"):
            break
        else:
            print("Please enter the below blood group types only.")
    while True:
        print()
        phone_no=input("Enter the patient's phone number: ")
        if phone_no.isdigit()==True:
            phone_no=int(phone_no)
            break
        else:
            print("Please enter only digit.")
    print()
    caretaker_name=input("Enter caretaker name: ")
    while True:
        print()
        caretaker_phone_no=input("Enter caretaker phone no: ")
        if caretaker_phone_no.isdigit()==True:
            caretaker_phone_no=int(caretaker_phone_no)
            break
        else:
            print("Please enter only digit.")
    print()
    doctor_name=input("Enter doctor name: ")
    while True:
        print()
        food_types=input("Enter the food type(veg or nonveg): ")
        if food_types.lower()=="veg":
            break
        elif food_types.lower()=="nonveg":
            break
        else:
            print("Please enter only veg or non veg.")
    print()
    print("The above detials have been updated")
    print()
    csr.execute("UPDATE Patients SET Name='%s',Age=%s,Gender='%s',Disease='%s',Blood_Group='%s',Phone_No=%s,Caretaker_Name='%s',Caretaker_Phone_No=%s,Doctor_Name='%s',Food_Types='%s' WHERE Aadhar_No=%s"%(name,age,gender,disease,blood_group,phone_no,caretaker_name,caretaker_phone_no,doctor_name,food_types,aadhar)) 
    cur.commit()

def InPatView():
    while True:
        print()
        aadhar=input("Enter the aadhar no of inpatient: ")
        if len(str(aadhar))==12:
            if aadhar.isdigit()==True:
                aadhar=int(aadhar)
                break
            else:
                print("Please enter only digit.")
        else:
            print("Please enter 12 digits.")
    while True:
        csr.execute("SELECT * FROM Patients WHERE Aadhar_No=%s"%aadhar)
        result=csr.fetchall()
        print()
        print("The name of the patient is",result[0][1],".")
        print()
        print("The age of the patient is",result[0][2],".")
        print()
        print("The gender of the patient is",result[0][3],".")
        print()
        print("The disease patient is enduring with is",result[0][4],".")
        print()
        print("The blood group of the patient is",result[0][5],".")
        print()
        print("The phone no of patient is",result[0][6],".")
        print()
        print("The caretaker name is",result[0][7],".")
        print()
        print("The caretaker phone no is",result[0][8],".")
        print()      
        print("The name of the doctor is",result[0][9],".")
        print()
        print("The food type is",result[0][10],".")
        print()
        break

def AuthAdd():
    while True:
        print()
        adhaar=input("Enter your unique 12 digit id number :")
        if len(str(adhaar))==12:
               if adhaar.isdigit()==True:
                   adhaar=int(adhaar)
                   break
               else:
                   print("Please enter only digits.")
        else:
            print("Please enter 12 digits.")
    while True:
        print()
        bed=input("Enter the number of beds available: ")
        if bed.isdigit()==True:
            bed=int(bed)
            break
        else:
            print("Please enter only Digits.")
    while True:
        print()
        bed1=input("Enter the total number of beds: ")
        if bed1.isdigit()==True:
            bed1=int(bed1)
            break
        else:
            print("Please enter only Digits.")
    while True:
        print()
        oxc=input("Enter the number of oxygen cylinders available: ")
        if oxc.isdigit()==True:
            oxc=int(oxc)
            break
        else:
            print("Please enter only Digits.")
    while True:
        print()
        vaca=input("Enter the number of vaccines available: ")
        if vaca.isdigit()==True:
            vaca=int(vaca)
            break
        else:
            print("Please enter only Digits.")
    while True:
        print()
        vacc=input("Enter the number of people vaccinated: ")
        if vacc.isdigit()==True:
            vacc=int(vacc)
            break
        else:
            print("Please enter only Digits.")
    while True:
        print()
        amba=input("Enter the number of ambulances available: ")
        if amba.isdigit()==True:
            amba=int(amba)
            break
        else:
            print("Please enter only Digits.")
    print()
    print("The above new details have been added")
    print()
    csr.execute("INSERT INTO Authorities(Adhaar_No,Beds_Available,Beds_Total,Oxygen_Cylinders,Vaccines_Available,Vaccinated,Ambulances) values(%s,%s,%s,%s,%s,%s,%s)"%(adhaar,bed,bed1,oxc,vaca,vacc,amba))
    cur.commit()

def AuthUpd():
    while True:
        print()
        adhaar=input("Enter your unique 12 digit id number: ")
        int3=csr.execute("Select Count(*) from Authorities where Aadhar_No=%s"%(int(aadhar)))
        if int3!=None:
            if len(str(adhaar))==12:
                   if adhaar.isdigit()==True:
                       adhaar=int(adhaar)
                       break
                   else:
                       print("Please enter 12 digits.")
            else:
                print("Please enter only digits")
        else:
            print("The above entered entered aadhar number is not in our database")
    while True:
        print()
        bed=input("Enter the number of beds available: ")
        if bed.isdigit()==True:
            bed=int(bed)
            break
        else:
            print("Please enter only Digits.")
    while True:
        print()
        bed1=input("Enter the total number of beds: ")
        if bed1.isdigit()==True:
            bed1=int(bed1)
            break
        else:
            print("Please enter only Digits.")
    while True:
        print()
        oxc=input("Enter the number of oxygen cylinders available: ")
        if oxc.isdigit()==True:
            oxc=int(oxc)
            break
        else:
            print("Please enter only Digits.")
    while True:
        print()
        vaca=input("Enter the number of vaccines available: ")
        if vaca.isdigit()==True:
            vaca=int(vaca)
            break
        else:
            print("Please enter only Digits.")
    while True:
        print()
        vacc=input("Enter the number of people vaccinated: ")
        if vacc.isdigit()==True:
            vacc=int(vacc)
            break
        else:
            print("Please enter only Digits.")
    while True:
        print()
        amba=input("Enter the number of ambulances available: ")
        if amba.isdigit()==True:
            amba=int(amba)
            break
        else:
            print("Please enter only Digits.")
    print()
    print("The above detials have been updated")
    print()
    csr.execute("UPDATE Authorities SET Beds_Available=%s,Beds_Total=%s,Oxygen_Cylinders=%s,Vaccines_Available=%s,Vaccinated=%s,Ambulances=%s WHERE Adhaar_No=%s"%(bed,bed1,oxc,vaca,vacc,amba,adhaar)) 
    cur.commit()

def AuthView():
     while True:
        csr.execute("SELECT * FROM Authorities")
        result=csr.fetchall()
        print()
        print("The no of beds available is ",result[0][1],".")
        print()
        print("The total no of beds avialable is ",result[0][2],".")
        print()
        print("The no of oxygen cylinders available is ",result[0][3],".")
        print()
        print("The no of vaccines available is ",result[0][4],".")
        print()
        print("The no of people vaccinated in your locality is ",result[0][5],".")
        print()
        print("The no of ambulances available is ",result[0][6],".")
        break

def CovDetAdd():
    while True:
        print()
        uid=input("Enter your unique 12 digit hospital id number: ")
        if len(str(uid))==12:
               if uid.isdigit()==True:
                   uid=int(uid)
                   break
               else:
                   print("Please enter only 12 digits.")
        else:
            print("Please enter 12 digits.")
    while True:
        print()
        cfm=input("Enter the number of confirmed cases: ")
        if cfm.isdigit()==True:
            cfm=int(cfm)
            break
        else:
            print("Please enter only Digits.")
    while True:
        print()
        act=input("Enter the number of active cases: ")
        if act.isdigit()==True:
            act=int(act)
            break
        else:
            print("Please enter only Digits.")
    while True:
        print()
        rcv=input("Enter the number of recovered cases: ")
        if rcv.isdigit()==True:
            rcv=int(rcv)
            break
        else:
            print("Please enter only Digits.")
    while True:
        print()
        dce=input("Enter the number of deceased cases: ")
        if dce.isdigit()==True:
            dce=int(dce)
            break
        else:
            print("Please enter only Digits.")
    while True:
        print()
        vac=input("Enter the number of people vaccinated: ")
        if vac.isdigit()==True:
            vac=int(vac)
            break
        else:
            print("Please enter only Digits.")
    print()
    print("The above details have been added")
    print()
    csr.execute("INSERT INTO Covid19_Details_Info(Unique_ID,Confirmed,Active,Recovered,Deceased,Vaccinated) values(%s,%s,%s,%s,%s,%s)"%(uid,cfm,act,rcv,dce,vac))
    cur.commit()

def CovDetUpd():
    while True:
        print()
        uid=input("Enter your unique 12 digit hospital id number: ")
        int4=csr.execute("Select Count(*) from Covid19_Details_Info where Unique_ID =%s"%(int(uid)))
        if int4!=None:
            if len(str(uid))==12:
                   if uid.isdigit()==True:
                       uid=int(uid)
                       break
                   else:
                       print("Please enter 12 digits.")
            else:
                print("Please enter only digits")
        else:
            print("The above entered entered aadhar number is not in our database")
    while True:
        print()
        cfm=input("Enter the number of confirmed cases: ")
        if cfm.isdigit()==True:
            cfm=int(cfm)
            break
        else:
            print("Please enter only Digits.")
    while True:
        print()
        act=input("Enter the number of active cases: ")
        if act.isdigit()==True:
            act=int(act)
            break
        else:
            print("Please enter only Digits.")
    while True:
        print()
        rcv=input("Enter the number of recovered cases: ")
        if rcv.isdigit()==True:
            rcv=int(rcv)
            break
        else:
            print("Please enter only Digits.")
    while True:
        print()
        dce=input("Enter the number of deceased cases: ")
        if dce.isdigit()==True:
            dce=int(dce)
            break
        else:
            print("Please enter only Digits.")
    while True:
        print()
        vac=input("Enter the number of people vaccinated: ")
        if vac.isdigit()==True:
            vac=int(vac)
            break
        else:
            print("Please enter only Digits.")
    print()
    print("The above details have been updated")
    print()
    csr.execute("UPDATE Covid19_Details_Info SET Confirmed=%s,Active=%s,Recovered=%s,Deceased=%s,Vaccinated=%s WHERE Unique_ID=%s"%(cfm,act,rcv,dce,vac,uid)) 
    cur.commit()

def CovDetView():
    while True:
        csr.execute("SELECT * FROM Covid19_Details_Info")
        result=csr.fetchall()
        print()
        print("The no of confirmed cases is",result[0][1],".")
        print()
        print("The no of active cases is ",result[0][2],".")
        print()
        print("The no of recovered cases is",result[0][3],".")
        print()
        print("The no of deceased cases is",result[0][4],".")
        print()
        print("The no of people vaccinated in your locality is",result[0][5],".")
        break

def CovPatAdd():
    while True:
        print()
        aadhar=input("Enter the aadhar no of outpatient: ")
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
    tresult=" "
    print()
    print("The above new details have been added")
    print()
    csr.execute("INSERT INTO Covid19_Patient_Info(Aadhar_No,name,Test_Result,Age,Phone_No) values(%s,'%s','%s',%s,%s)"%(aadhar,name,tresult,age,phone_no))
    cur.commit()

def CovPatUpd():
    while True:
        print()
        aadhar=input("Enter the aadhar no of outpatient: ")
        int5=csr.execute("Select Count(*) from Covid19_Patient_Info where Aadhar_no=%s"%(int(aadhar)))
        if int5!=None:
            if len(str(aadhar))==12:
                if aadhar.isdigit()==True:
                    aadhar=int(aadhar)
                    break
                else:
                    print("Please enter only digit.")
            else:
                print("Please enter 12 digits.")
        else:
            print("The above entered entered aadhar number is not in our database")
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

def CovPatView():
    while True:
        print()
        aadhar=input("Enter your aadhar number of outpatient: ")
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
        print("If there is no result it means that the result of the Covid19Test has still not come out")
        break
    
A='''

                                                           STRENGTH DOES NOT COME FROM PHYSICAL CAPACITY.
                                                           ----------------------------------------------
                                                                  IT COMES FROM AN INDOMITABLE WILL.
                                                                  ----------------------------------
      '''

B='''
        
                                                         LIFE IS NOT ABOUT WAITING FOR THE STORM TO PASS,
                                                         ------------------------------------------------
                                                           IT IS ABOUT LEARNING HOW TO DANCE IN THE RAIN.
                                                           ----------------------------------------------
      '''

C='''

                                                            YOU CAN STILL MAKE SOMETHING BEAUTIFUL AND
                                                            ------------------------------------------
                                                          SOMETHING POWERFUL OUT OF A REALLY BAD SITUATION.
                                                          -------------------------------------------------
      '''

D='''
                                                            STAY POSITIVE.BETTER DAYS ARE ON THEIR WAY.
                                                            -------------------------------------------
      '''

E='''

                                                             YOU ARE BRAVER THAN YOU BELEIVE, STRONGER 
                                                             -----------------------------------------
                                                             THAN YOU SEEM AND SMARTER THAN YOU THINK.
                                                             -----------------------------------------
      '''

thoughts=[A,B,C,D,E]
T=random.randint(0,4)
print(thoughts[T])

print('''
                     _______              _______  ________            ______       __________   ________                       ______   _____  
   \              / |          |         |        |        | |\    /| |                  |      |        |     |  / \        / |        |
    \            /  |          |         |        |        | | \  / | |                  |      |        |     | /   \      /  |______  |_____
     \    /\    /   |_______   |         |        |        | |  \/  | |______            |      |        |     |/     \    /          |       |
      \  /  \  /    |          |         |        |        | |      | |                  |      |        |     |\      \  /           |       |
       \/    \/     |_______   |________ |_______ |________| |      | |______            |      |________|     | \      \/      ______|  _____|      
   ---------------------------------------------------------------------------------------------------------------------------------------------    
   ---------------------------------------------------------------------------------------------------------------------------------------------
                                                    ______   _____   ______   ___ ___  _______         
                                           |     | |      | |       |      |     |        |         /\      |
                                           |     | |      | |_____  |______|     |        |        /  \     |
                                           |-----| |      |       | |            |        |       /----\    |
                                           |     | |      |       | |            |        |      /      \   |
                                           |     | |______|  _____| |         ___|___     |     /        \  |_______
                                         ----------------------------------------------------------------------------
                                         ----------------------------------------------------------------------------
        ''')

while True:
    print("""

              ______________          _______________          _______________          _______________          _______________         
             |              |        |               |        |               |        |               |        |               |
             | 1.OUTPATIENT |        |  2.INPATIENT  |        | 3.AUTHORITIES |        |   4.DOCTOR    |        |    5.EXIT     |
             |______________|        |_______________|        |_______________|        |_______________|        |_______________|


          """)

    n1=int(input("Enter the choice"))
    
    if n1==1:
        print()
        print("Hello OUTPATIENT")
        while True:
            print("""
                        ##====================================##  
                        ||                                    ||
                        ||  CHOOSE ONE OF THE GIVEN OPTION :- ||
                        ||____________________________________||
                        ||                                    ||
                        || 1. Covid-19 Test Results           ||
                        || 2. Covid-19 Test Takers            ||
                        || 3. Covid-19 Daily Tracker          ||
                        || 4. Hospital Equipment Details      ||
                        || 5. Back                            ||
                        ||                                    ||
                        ##====================================##
                  """)
            choice=int(input("Enter your choice"))
            if choice==1:
                CovPatView()
                break
            elif choice==2:
                CovPatAdd()
                break
            elif choice==3:
                CovDetView()
                break
            elif choice==4:
                AuthView()
                break
            elif choice==5:
                break
            else:
                print()
                print("""~!~!~!~WRONG CHOICE PLEASE ENTER VALID VALUE~!~!~!~""")
                       
    elif n1==2:
        print()
        print("Hello INPATIENT")
        while True:
            print("""
                        ##====================================##  
                        ||                                    ||
                        ||  CHOOSE ONE OF THE GIVEN OPTION :- ||
                        ||____________________________________||
                        ||                                    ||
                        || 1. Patient Information             ||
                        || 2. Hospital Equipment Details      ||
                        || 3. Covid-19 Daily Tracker          ||
                        || 4. Back                            ||
                        ||                                    ||
                        ##====================================##
                  """)
            choice=int(input("Enter your choice"))
            if choice==1:
                InPatView()
                break
            elif choice==2:
                AuthView()
                break
            elif choice==3:
                CovDetView()
                break
            elif choice==4:
                break
            else:
                print()
                print("""~!~!~!~WRONG CHOICE PLEASE ENTER VALID VALUE~!~!~!~""")
        
    elif n1==3:
        print()
        print("Hello AUTHORITIES")
        while True:
            print("""                                       
                        ##===========================================##  
                        ||                                           ||
                        ||      CHOOSE ONE OF THE GIVEN OPTION :-    ||
                        ||___________________________________________||
                        ||                                           ||
                        || 1. Hospital Equipment Details             ||
                        || 2. Add Details of hospital equipment      ||
                        || 3. Update Details of hospital equipment   ||
                        || 4. Patient Information                    ||
                        || 5. Doctor Information                     ||
                        || 6. Covid-19 Daily Tracker                 ||
                        || 7. Back                                   ||
                        ||                                           ||
                        ##===========================================##
                  """)
            choice=int(input("Enter your choice"))
            if choice==1:
                AuthView()
                break
            elif choice==2:
                AuthAdd()
                break
            elif choice==3:
                AuthUpd()
                break
            elif choice==4:
                InPatView()
                break
            elif choice==5:
                DocView()
                break
            elif choice==6:
                CovDetView()
                break
            elif choice==7:
                break
            else:
                print()
                print("""~!~!~!~WRONG CHOICE PLEASE ENTER VALID VALUE~!~!~!~""")
           
    elif n1==4:
        print("Hello DOCTOR")
        while True:
            print("""                                    
                        ##==============================================##  
                        ||                                              ||
                        ||       CHOOSE ONE OF THE GIVEN OPTION :-      ||
                        ||______________________________________________||
                        ||                                              ||
                        || 1.  Doctor Information                       ||
                        || 2.  Add Doctor Information                   ||
                        || 3.  Update Doctor Information                ||
                        || 4.  Patient Information                      ||
                        || 5.  Add Patient Information                  ||
                        || 6.  Update Patient Information               ||
                        || 7.  Covid-19 Daily Tracker                   ||
                        || 8.  Add Details for Covid-19 Daily Tracker   ||
                        || 9.  Update Covid-19 Daily Tracker            ||
                        || 10. Hospital Equipment Details               ||
                        || 11. Update Details of Hospital Equipment     ||
                        || 12. Covid-19 Test Results                    ||
                        || 13. Update Covid-19 Test Results             ||
                        || 14. Back                                     ||
                        ||                                              ||
                        ##==============================================##
                  """)
            choice=int(input("Enter your choice"))
            if choice==1:
                DocView()
                break
            elif choice==2:
                DocAdd()
                break
            elif choice==3:
                DocUpd()
                break
            elif choice==4:
                InPatView()
                break
            elif choice==5:
                InPatAdd()
                break
            elif choice==6:
                InPatUpd()
                break
            elif choice==7:
                CovDetView()
                break
            elif choice==8:
                CovDetAdd()
                break
            elif choice==9:
                CovDetUpd()
                break
            elif choice==10:
                AuthView()
                break
            elif choice==11:
                AuthUpd()
                break
            elif choice==12:
                CovPatView()
                break
            elif choice==13:
                CovPatUpd()
                break
            elif choice==14:
                break
            else:
                print()
                print("""~!~!~!~WRONG CHOICE PLEASE ENTER VALID VALUE~!~!~!~""")

    elif n1==5:
        print()
        print("EXITIING!")
        print("Thank You for visiting us, wishing you a healthy life and speedy recovery")
        break

    else:
        print()
        print("""~!~!~!~WRONG CHOICE PLEASE ENTER VALID VALUE~!~!~!~""")
    
     
        

            






             





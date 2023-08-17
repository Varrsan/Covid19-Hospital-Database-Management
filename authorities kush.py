#warnings for the doctor and authority to be done later
import mysql.connector
cur=mysql.connector.connect(host="localhost",user="root",passwd="varrsan123",database="project20")
csr=cur.cursor()

csr.execute("CREATE table Authorities(Adhaar_No BIGINT,Beds_Available INT,Beds_Total INT,Oxygen_Cylinders INT,Vaccines_Available INT,Vaccinated INT,Ambulances INT)")
def authorities_info():
    while True:
        print()
        ask=input("Select any of the three options:\n"
                  "1.E for entering new details\n"
                  "2.U for updating a doctor's details\n"
                  "3.V for Viewing Details of a doctor\n"
                  "4.X For Exiting\n"

                  "Type in your answer: ")
        if ask.lower()=="e":
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
        elif ask.lower()=="u":
            while True:
                print()
                adhaar=input("Enter your unique 12 digit id number: ")
                if len(str(adhaar))==12:
                       if adhaar.isdigit()==True:
                           adhaar=int(adhaar)
                           break
                       else:
                           print("Please enter 12 digits.")
                else:
                    print("Please enter only digits")   
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
        elif ask.lower()=="v":
             while True:
                print()
                adhaar=input("Enter your ADHAAR number: ")
                if len(str(adhaar))==12:
                       if adhaar.isdigit()==True:
                           adhaar=int(adhaar)
                           break
                       else:
                           print("Please enter only digits.")
                else:
                    print("Please enter 12 digits")
             while True:
                csr.execute("SELECT * FROM Authorities WHERE Adhaar_No=%s"%adhaar)
                result=csr.fetchall()
                print()
                print("The aadhaarno is ",result[0][0],".")
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
        elif ask.lower()=="x":
            print()
            print("Thank You!!")
            break
        else:
            print()
            print("Enter only E,U,V or X.")
authorities_info()           

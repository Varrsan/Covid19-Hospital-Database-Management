#warnings for the doctor and authority to be done later
import mysql.connector
cur=mysql.connector.connect(host="localhost",user="root",passwd="varrsan123",database="project13")
csr=cur.cursor()
csr.execute("CREATE table Covid19_Details_Info(Unique_ID BIGINT,Confirmed INT,Active INT,Recovered INT,Deceased INT,Vaccinated INT)")
def covidinfo():
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
        elif ask.lower()=="u":
            while True:
                print()
                uid=input("Enter your unique 12 digit hospital id number: ")
                if len(str(uid))==12:
                       if uid.isdigit()==True:
                           uid=int(uid)
                           break
                       else:
                           print("Please enter 12 digits.")
                else:
                    print("Please enter only digits") 
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
        elif ask.lower()=="v":
            while True:
                print()
                uid=input("Enter your unique 12 digit hospital id number:")
                if len(str(uid))==12:
                       if uid.isdigit()==True:
                           uid=int(uid)
                           break
                       else:
                           print("Please enter only digits.")
                else:
                    print("Please enter 12 digits")
            while True:
                csr.execute("SELECT * FROM Covid19_Details_Info WHERE Unique_ID=%s"%uid)
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
        elif ask.lower()=="x":
            print()
            print("Thank You!!")
            break
        else:
            print()
            print("Enter only N,U,S or E.")
covidinfo()           

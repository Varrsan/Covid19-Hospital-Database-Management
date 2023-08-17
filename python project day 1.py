import mysql.connector
cur=mysql.connector.connect(host="localhost",user="root",passwd="varrsan123",database="project13")
csr=cur.cursor()

csr.execute("CREATE table covid19detailsinfo7(KEY int,confirmed int,active int,recovered int,deceased int,vaccinated int)")
def covid19info():
    while True:
        c=input("Do you want enter new values(Enter N) or update values(Enter U) or see the values(Enter S)?")
        if c.lower()=='n':
            while True:
                key=input("Enter the key")
                if key.isdigit()==True:
                    key=int(key)
                    print("Key is approved")
                    break
                else:
                    print("Enter please enter only digits")
            while True:
                dce=input("Enter the no of deceased")
                if dce.isdigit()==True :
                    dce=int(dce)
                    break
                else:
                    print("Please enter only digits")
            while True:
                cfm=input("Enter the no of confirmed cases")
                if cfm.isdigit()==True :
                    cfm=int(cfm)
                    break
                else:
                    print("Please enter only digits")
            while True:
                act=input("Enter the no of active cases")                                                              
                if act.isdigit()==True :
                    act=int(act)
                    break
                else:
                    print("Please enter only digits")
            while True:
                rcv=input("Enter the no of people recovered")
                if rcv.isdigit()==True :
                    rcv=int(rcv)
                    break
                else:
                    print("Please enter only digits")
            while True:
                vac=input("Enter the no of people vaccinated")
                if vac.isdigit()==True :
                    vac=int(vac)
                    break
                else:
                    print("Please enter only digits")
            csr.execute("insert into covid19detailsinfo7(KEY,confirmed,active,recovered,deceased,vaccinated) values(%s,%s,%s,%s,%s,%s)"%(key,cfm,act,rcv,dce,vac))
            cur.commit()
            
        elif c.lower()=='u':
            while True:
                key=input("Enter the key")
                if key.isdigit()==True:
                    key=int(key)
                    print("Key is approved")
                    break
                else:
                    print("Enter please enter only digits")
            while True:
                dce=input("Enter the no of deceased")
                if dce.isdigit()==True :
                    dce=int(dce)
                    break
                else:
                    print("Please enter only digits")
            while True:
                cfm=input("Enter the no of confirmed cases")
                if cfm.isdigit()==True :
                    cfm=int(cfm)
                    break
                else:
                    print("Please enter only digits")
            while True:
                act=input("Enter the no of active cases")                                                              
                if act.isdigit()==True :
                    act=int(act)
                    break
                else:
                    print("Please enter only digits")
            while True:
                rcv=input("Enter the no of people recovered")
                if rcv.isdigit()==True :
                    rcv=int(rcv)
                    break
                else:
                    print("Please enter only digits")
            while True:
                vac=input("Enter the no of people vaccinated")
                if vac.isdigit()==True :
                    vac=int(vac)
                    break
                else:
                    print("Please enter only digits")

            csr.execute("UPDATE covid19detailsinfo7 SET confimed=%s,active=%s,recovered=%s,deceased=%s,vaccinated=%s WHERE KEY=%s"%(cfm,act,rcv,dce,vac,key))
            cur.commit()
                        
        elif c.lower()=='s':
            while True:
                key=input("Enter the key")
                if key.isdigit()==True:
                    key=int(key)
                    print("Key is approved")
                    break
                else:
                    print("Enter please enter only digits")
            while True:
                csr.execute("SELECT * FROM covid19detailsinfo7 WHERE KEY=%s"%key)
                result=csr.fetchall()
                print("The no of confirmed cases is ",result[0][1],".")
                print()
                print("The total no of active cases is ",result[0][2],".")
                print()
                print("The no of recovered cases is ",result[0][3],".")
                print()
                print("The no of deceased cases is ",result[0][4],".")
                print()
                print("The no of people vaccinated in your locality is ",result[0][5],".")
                break

        elif c.lower()=="e":
            print("Thankyou!!")
            break

        else:
            print("Enter only N,U,S or E.")
     
           
covid19info()

              




                       

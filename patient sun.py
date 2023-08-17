import mysql.connector
cur=mysql.connector.connect(host="localhost",user="root",password="varrsan123",database="sundar3")
csr=cur.cursor()
csr.execute("CREATE table Patients(Aadhar_No BIGINT,Name VARCHAR(20),Age INT,Gender VARCHAR(20),Disease VARCHAR(20),Blood_Group VARCHAR(20),Phone_No BIGINT,Caretaker_Name VARCHAR(20),Caretaker_Phone_No BIGINT,Doctor_Name VARCHAR(20),Food_Types VARCHAR(20))")
def patients():
    while True:
        ask = input("Select any of the three options:\n"
                   "1.E for entering new details\n"
                   "2.U for updating a doctor's details\n"
                   "3.V for Viewing Details of a doctor\n"
                   "4.X For Exiting\n"

                   "Type in your answer: ") 
        if ask.lower()=='e':
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
        elif ask.lower()=="v":
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
        elif ask.lower()=="x":
            print()
            print("THANKYOU WISHING YOU A BEST HEALTH AND SPEEDY RECOVERY.")
            break
        else:
            print()
            print("Enter only E,U,V or X.")
patients()
                        
                        
                        
                        
                        
                        
                        
                             
                             
                            

                            
        
               
                            
               
                
            
        
                
                
                
                
                
              
            
            
            
                             
            
                    
    
    

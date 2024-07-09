#Main Class
from colorama import init, Fore, Back, Style
import json
import mysql.connector
class Main:
# Function to register the Account.
    def registerAccount():
        def load_json(file_path):
            #Inputs --->
            name= input(Fore.LIGHTGREEN_EX+" NAME "+Style.RESET_ALL+":")
            def cityInput():
                cities = ["Coimbatore", "Chennai", "Madurai", "Tiruchirappalli", "Salem", "Tiruppur", "Erode", "Vellore", "Tirunelveli", "Thoothukudi", "Nagercoil", "Thanjavur", "Dindigul", "Cuddalore", "Kanchipuram", "Tiruvannamalai", "Kumbakonam", "Pudukkottai", "Karaikudi", "Pollachi", "Namakkal", "Rajapalayam", "Sivakasi", "Karur", "Ooty", "Kanyakumari", "Chidambaram", "Neyveli", "Kodaikanal", "Rameswaram", "Hosur", "Kovilpatti", "Nagapattinam", "Theni", "Udhagamandalam", "Sirkali", "Arakkonam", "Tiruvallur", "Mayiladuthurai", "Virudhunagar", "Pondicherry", "Ariyalur", "Tindivanam", "Sankarankovil", "Vaniyambadi", "Perambalur", "Pattukkottai", "Namagiripettai", "Metupalayam", "Palladam", "Tenkasi", "Villupuram", "Sathyamangalam", "Gobichettipalayam", "Nellai", "Mettur", "Ranipet", "Thiruvarur", "Sankarapuram", "Karaikkudi", "Tambaram", "Walajapet", "Poonamallee", "Avadi", "Thiruthani", "Gudiyattam", "Bhavani", "Papanasam", "Ambasamudram", "Ramanathapuram", "Paramakudi", "Vridhachalam", "SankaranKoil", "Udumalpet", "Neyveli Township", "Kuniyamuthur", "Kallakurichi", "Jambai", "Edaikodu", "Valparai"]
                city=input(Fore.LIGHTGREEN_EX+" CITY "+Style.RESET_ALL+":")
                city = city[0].upper() + city[1:].lower()
                if (city not in cities):
                    print(Fore.RED +"You have entered the name incorrectly! Try again"+Style.RESET_ALL)
                    city = cityInput()
                return city
            city = cityInput()
                
            BloodGroup = input(Fore.LIGHTRED_EX+" BLOOD GROUP "+Style.RESET_ALL+":").upper()
            
            MobileNo= (input(Fore.LIGHTGREEN_EX+" CELL NO "+Style.RESET_ALL+":"))
            
            #MYSQL DB
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Vikkramvikky#0821',
                database='BloodDonors'
                )
    
            cursor = connection.cursor()
            
            delete_query = f"INSERT INTO CITIES (NAME,PhoneNumber,CityName,BloodGroup) VALUES (%s,%s,%s,%s);"
            cursor.execute(insert_query,(name,MobileNo,city,BloodGroup))
            
            connection.commit()
            cursor.close()
            connection.close()
            
            #Open File --->
            # with open(file_path, 'r', encoding='utf-8') as f:
                  
            #     data = json.load(f)
            #     data[BloodGroup][city][name] = MobileNo
                
            #     print("--------------------------------------------------------------------------------------------------------------------------------------------------------------")
            #     print(f"{Fore.YELLOW}Your details has been registered... {Fore.CYAN}Name:{name},Blood Group:{BloodGroup},Mobile No.{MobileNo}, City:{city}{Style.RESET_ALL}")
            #     print("--------------------------------------------------------------------------------------------------------------------------------------------------------------")
            # with open(file_path, 'w') as f:
            #     json.dump(data, f, indent=4)


        file_path = "Database.json"
        load_json(file_path)

    
#----------------------------------------------------------------------------------------------------
#Funtion to display the details of a person in a particular City.
    def bloodInCity():
        #list of cities
        cities = ["Coimbatore", "Chennai", "Madurai", "Tiruchirappalli", "Salem", "Tiruppur", "Erode", "Vellore", "Tirunelveli", "Thoothukudi", "Nagercoil", "Thanjavur", "Dindigul", "Cuddalore", "Kanchipuram", "Tiruvannamalai", "Kumbakonam", "Pudukkottai", "Karaikudi", "Pollachi", "Namakkal", "Rajapalayam", "Sivakasi", "Karur", "Ooty", "Kanyakumari", "Chidambaram", "Neyveli", "Kodaikanal", "Rameswaram", "Hosur", "Kovilpatti", "Nagapattinam", "Theni", "Udhagamandalam", "Sirkali", "Arakkonam", "Tiruvallur", "Mayiladuthurai", "Virudhunagar", "Pondicherry", "Ariyalur", "Tindivanam", "Sankarankovil", "Vaniyambadi", "Perambalur", "Pattukkottai", "Namagiripettai", "Metupalayam", "Palladam", "Tenkasi", "Villupuram", "Sathyamangalam", "Gobichettipalayam", "Nellai", "Mettur", "Ranipet", "Thiruvarur", "Sankarapuram", "Karaikkudi", "Tambaram", "Walajapet", "Poonamallee", "Avadi", "Thiruthani", "Gudiyattam", "Bhavani", "Papanasam", "Ambasamudram", "Ramanathapuram", "Paramakudi", "Vridhachalam", "SankaranKoil", "Udumalpet", "Neyveli Township", "Kuniyamuthur", "Kallakurichi", "Jambai", "Edaikodu", "Valparai"]
        #Inputs --->
        blood=input(f"{Fore.LIGHTRED_EX}Enter the Blood Group{Style.RESET_ALL} (O+,O-,A+,A-,B+,B-,AB+,AB-): ").upper()
        def cityInput():
                cities = ["Coimbatore", "Chennai", "Madurai", "Tiruchirappalli", "Salem", "Tiruppur", "Erode", "Vellore", "Tirunelveli", "Thoothukudi", "Nagercoil", "Thanjavur", "Dindigul", "Cuddalore", "Kanchipuram", "Tiruvannamalai", "Kumbakonam", "Pudukkottai", "Karaikudi", "Pollachi", "Namakkal", "Rajapalayam", "Sivakasi", "Karur", "Ooty", "Kanyakumari", "Chidambaram", "Neyveli", "Kodaikanal", "Rameswaram", "Hosur", "Kovilpatti", "Nagapattinam", "Theni", "Udhagamandalam", "Sirkali", "Arakkonam", "Tiruvallur", "Mayiladuthurai", "Virudhunagar", "Pondicherry", "Ariyalur", "Tindivanam", "Sankarankovil", "Vaniyambadi", "Perambalur", "Pattukkottai", "Namagiripettai", "Metupalayam", "Palladam", "Tenkasi", "Villupuram", "Sathyamangalam", "Gobichettipalayam", "Nellai", "Mettur", "Ranipet", "Thiruvarur", "Sankarapuram", "Karaikkudi", "Tambaram", "Walajapet", "Poonamallee", "Avadi", "Thiruthani", "Gudiyattam", "Bhavani", "Papanasam", "Ambasamudram", "Ramanathapuram", "Paramakudi", "Vridhachalam", "SankaranKoil", "Udumalpet", "Neyveli Township", "Kuniyamuthur", "Kallakurichi", "Jambai", "Edaikodu", "Valparai"]
                city=input(f"{Fore.LIGHTGREEN_EX}City:")
                city = city[0].upper() + city[1:].lower()
                if (city not in cities):
                    print(Fore.RED +"You have entered the name incorrectly! Try again"+Style.RESET_ALL)
                    city = cityInput()
                return city
        city = cityInput()
                
                
        #Displaying Output
        file_path = "Database.json"
        
        #MYSQL DB
        
        connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Vikkramvikky#0821',
                database='BloodDonors'
                )
    
        cursor = connection.cursor()
        
        query = f"SELECT NAME, PhoneNumber, CityName, BloodGroup FROM cities WHERE cityname = %s AND bloodgroup = %s;"
        cursor.execute(query,(city,blood))
        
        rows = cursor.fetchall()
        for i,row in enumerate(rows):
                print(Fore.MAGENTA+"DONOR-",i,""+Style.RESET_ALL)
                print(Fore.LIGHTBLUE_EX+"------------------------------------------------")
                print(Fore.LIGHTBLUE_EX+"DONOR Name: "+Fore.LIGHTWHITE_EX,row[0],""+Style.RESET_ALL)
                print(Fore.LIGHTBLUE_EX+"Mobile Number:"+Fore.LIGHTWHITE_EX,row[1],""+Style.RESET_ALL)
                print(Fore.LIGHTBLUE_EX+"District "     +Fore.LIGHTWHITE_EX,row[2],""+Style.RESET_ALL)
                print(Fore.LIGHTBLUE_EX+"Blood Group: " +Fore.LIGHTWHITE_EX,row[3],""+Style.RESET_ALL)
                print(Fore.LIGHTBLUE_EX+"------------------------------------------------"+Style.RESET_ALL)
                
                print("")
                print("")
        cursor.close()
        connection.close()
        
        # with open(file_path, 'r', encoding='utf-8') as f:
        #         data = json.load(f)
        #         print(f"{Fore.LIGHTBLACK_EX}"+json.dumps(data[blood][city], indent=4))
        
#----------------------------------------------------------------------------------------------------
#Funtion to list Required blood in all cities
    def bloodInAllCities():
        
        blood=input(f"{Fore.LIGHTRED_EX}Enter the Blood Group{Style.RESET_ALL} (O+,O-,A+,A-,B+,B-,AB+,AB-): ").upper()
        
        #MYSQL DB
        
        connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Vikkramvikky#0821',
                database='BloodDonors'
                )
    
        cursor = connection.cursor()
        
        query = f"SELECT NAME, PhoneNumber, CityName, BloodGroup FROM cities WHERE bloodgroup = %s;"
        cursor.execute(query,(blood,))
        
        rows = cursor.fetchall()
        for i,row in enumerate(rows):
                print(Fore.MAGENTA+"DONOR-",i,""+Style.RESET_ALL)
                print(Fore.LIGHTBLUE_EX+"------------------------------------------------")
                print(Fore.LIGHTBLUE_EX+"DONOR Name: "+Fore.LIGHTWHITE_EX,row[0],""+Style.RESET_ALL)
                print(Fore.LIGHTBLUE_EX+"Mobile Number:"+Fore.LIGHTWHITE_EX,row[1],""+Style.RESET_ALL)
                print(Fore.LIGHTBLUE_EX+"District "     +Fore.LIGHTWHITE_EX,row[2],""+Style.RESET_ALL)
                print(Fore.LIGHTBLUE_EX+"Blood Group: " +Fore.LIGHTWHITE_EX,row[3],""+Style.RESET_ALL)
                print(Fore.LIGHTBLUE_EX+"------------------------------------------------"+Style.RESET_ALL)
                
                print("")
                print("")
        cursor.close()
        connection.close()
        
        
        # file_path = "Database.json"
        # with open(file_path, 'r', encoding='utf-8') as f:
        #         data = json.load(f)
        #         print(Fore.LIGHTCYAN_EX+json.dumps(data[blood], indent=4))
#----------------------------------------------------------------------------------------------------
#Funtion to display the matchin bloods.
    def bloodMatch():
        possibleBloods={"O+":{"O+","O-"},
                        "O-":{"O-"},
                        "A+":{"O+","O-","A+","A-"},
                        "A-":{"O-","A-"},
                        "B+":{"O+","O-","B+","B-"},
                        "B-":{"O-","B-"},
                        "AB+":{"O+","O-","A+","A-","B+","B-","AB+","AB-"},
                        "AB-":{"O-","A-","B-","AB-"}
                        }
        donorMap = {
                        "O+": {"O+", "A+", "B+", "AB+"},
                        "O-": {"O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"},
                        "A+": {"A+", "AB+"},
                        "A-": {"A+", "A-", "AB+", "AB-"},
                        "B+": {"B+", "AB+"},
                        "B-": {"B+", "B-", "AB+", "AB-"},
                        "AB+": {"AB+"},
                        "AB-": {"AB+", "AB-"}
}

        blood=input(f"{Fore.LIGHTRED_EX}Enter the Blood Group{Style.RESET_ALL} (O+,O-,A+,A-,B+,B-,AB+,AB-): ").upper()
        print("1. POSSIBLE DONOR BLOOD GROUP")
        print("2. POSSIBLE RECEIPTANT BLOOD GROUP")
        
        def bloodPossiblity():
                n = int(input("Enter Either 1 or 2:"))
                if(n==1):
                    print("--------------------------------------------------------------------------------")
                    print('"'+f"{Fore.LIGHTYELLOW_EX}You can get a Donor of {Fore.MAGENTA}{list(possibleBloods[blood])}{Fore.LIGHTYELLOW_EX} groups."+'"')
                    print(Style.RESET_ALL+"--------------------------------------------------------------------------------")
                elif(n==2):
                    print("--------------------------------------------------------------------------------")
                    print('"'+f"{Fore.LIGHTYELLOW_EX}You can Donate to {Fore.MAGENTA}{list(donorMap[blood])}{Fore.LIGHTYELLOW_EX} groups."+'"')
                    print(Style.RESET_ALL+"--------------------------------------------------------------------------------")
                else:
                    print("Wrong Number. Enter 1 or 2 ")
                    bloodPossiblity()
        bloodPossiblity()

#----------------------------------------------------------------------------------------------------
    def showAllInCity():
        def cityInput():
                cities = ["Coimbatore", "Chennai", "Madurai", "Tiruchirappalli", "Salem", "Tiruppur", "Erode", "Vellore", "Tirunelveli", "Thoothukudi", "Nagercoil", "Thanjavur", "Dindigul", "Cuddalore", "Kanchipuram", "Tiruvannamalai", "Kumbakonam", "Pudukkottai", "Karaikudi", "Pollachi", "Namakkal", "Rajapalayam", "Sivakasi", "Karur", "Ooty", "Kanyakumari", "Chidambaram", "Neyveli", "Kodaikanal", "Rameswaram", "Hosur", "Kovilpatti", "Nagapattinam", "Theni", "Udhagamandalam", "Sirkali", "Arakkonam", "Tiruvallur", "Mayiladuthurai", "Virudhunagar", "Pondicherry", "Ariyalur", "Tindivanam", "Sankarankovil", "Vaniyambadi", "Perambalur", "Pattukkottai", "Namagiripettai", "Metupalayam", "Palladam", "Tenkasi", "Villupuram", "Sathyamangalam", "Gobichettipalayam", "Nellai", "Mettur", "Ranipet", "Thiruvarur", "Sankarapuram", "Karaikkudi", "Tambaram", "Walajapet", "Poonamallee", "Avadi", "Thiruthani", "Gudiyattam", "Bhavani", "Papanasam", "Ambasamudram", "Ramanathapuram", "Paramakudi", "Vridhachalam", "SankaranKoil", "Udumalpet", "Neyveli Township", "Kuniyamuthur", "Kallakurichi", "Jambai", "Edaikodu", "Valparai"]
                city=input(f"{Fore.LIGHTGREEN_EX}City:")
                city = city[0].upper() + city[1:].lower()
                if (city not in cities):
                    print(Fore.RED +"You have entered the name incorrectly! Try again"+Style.RESET_ALL)
                    city = cityInput()
                return city
        city = cityInput()
        
        Bloods = ["O+","O-","A+","A-","B+","B-","AB+","AB-"]
        
        #MYSQL DB
        connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Vikkramvikky#0821',
                database='BloodDonors'
                )
    
        cursor = connection.cursor()
        
       
        for blood in Bloods:
            print(Back.BLACK+Fore.WHITE+"__________________[",blood,"]__________________"+Style.RESET_ALL)
            query = f"SELECT NAME, PhoneNumber, CityName, BloodGroup FROM cities WHERE CityName = %s AND BloodGroup = %s;"
            cursor.execute(query,(city,blood))
            rows = cursor.fetchall()
            
            for i,row in enumerate(rows):
                print(Fore.RED+"DONOR-",i,""+Style.RESET_ALL)
                print(Fore.LIGHTBLUE_EX+"------------------------------------------------")
                print(Fore.LIGHTBLUE_EX+"DONOR Name: "+Fore.LIGHTWHITE_EX,row[0],""+Style.RESET_ALL)
                print(Fore.LIGHTBLUE_EX+"Mobile Number:"+Fore.LIGHTWHITE_EX,row[1],""+Style.RESET_ALL)
                print(Fore.LIGHTBLUE_EX+"District "     +Fore.LIGHTWHITE_EX,row[2],""+Style.RESET_ALL)
                print(Fore.LIGHTBLUE_EX+"Blood Group: " +Fore.LIGHTWHITE_EX,row[3],""+Style.RESET_ALL)
                print(Fore.LIGHTBLUE_EX+"------------------------------------------------"+Style.RESET_ALL)
                
                print("")
                print("")
                
        cursor.close()
        connection.close()
        
        
        
        # for blood in Bloods:
        #     with open("Database.json","r",encoding="utf-8") as f:
        #         data=json.load(f)
        #         print(Back.BLACK+Fore.WHITE+"_____________[",blood,"]_____________"+Style.RESET_ALL)
        #         print(Fore.LIGHTCYAN_EX+json.dumps(data[blood][city],indent=4))

#----------------------------------------------------------------------------------------------------

    def displayInfo():
        #  with open("Database.json","r",encoding="utf-8") as f:
        #         data=json.load(f)
        #         for i in range(1,data["Count"]+1):
        #               print(Fore.LIGHTBLACK_EX+json.dumps(data["Emergency"][str(i)],indent=4))
         #MYSQL DB
        
        connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Vikkramvikky#0821',
                database='BloodDonors'
                )
    
        cursor = connection.cursor()
        
        query = f"SELECT PatientName, District,BloodGroup, HospitalName, ContactNo FROM Emergency;"
        cursor.execute(query)
        
        rows = cursor.fetchall()
        for i,row in enumerate(rows):
                print(Fore.LIGHTBLACK_EX+"Patient-",i,""+Style.RESET_ALL)
                print(Fore.LIGHTBLUE_EX+"------------------------------------------------")
                print(Fore.LIGHTBLUE_EX+"PatientName: "+Fore.LIGHTWHITE_EX,row[0],""+Style.RESET_ALL)
                print(Fore.LIGHTBLUE_EX+"District:"+Fore.LIGHTWHITE_EX,row[1],""+Style.RESET_ALL)
                print(Fore.LIGHTBLUE_EX+"Blood Group:"     +Fore.LIGHTWHITE_EX,""+Fore.RED,row[2],""+Style.RESET_ALL)
                print(Fore.YELLOW+"Hospital Name:" +Fore.LIGHTWHITE_EX,row[3],""+Style.RESET_ALL)
                print(Fore.YELLOW+"Contact No: " +Fore.LIGHTWHITE_EX,row[4],""+Style.RESET_ALL)
                print(Fore.LIGHTBLUE_EX+"------------------------------------------------"+Style.RESET_ALL)
                
                print("")
                print("")
        cursor.close()
        connection.close()
        
#----------------------------------------------------------------------------------------------------
    def updateEmergencyDetaisl():
        def load_json(file_path):
            
            patientName = input("Enter the Patient Name: ")
            district= input("Enter the District Name: ")
            bloodGroup= input("Enter the Blood Group of patient: ")
            hospitalName= input("Enter the Hospital Name: ")
            cotactNumber= input("Enter the Contact Number: ")


            #MYSQL DB
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Vikkramvikky#0821',
                database='BloodDonors'
                )
    
            cursor = connection.cursor()
            
            delete_query = f"INSERT INTO Emergency (PatientName, District, BloodGroup, HospitalName, ContactNo) VALUES (%s,%s,%s,%s,%s);"
            cursor.execute(insert_query,(patientName,district,bloodGroup,hospitalName,cotactNumber))
            
            connection.commit()
            cursor.close()
            connection.close()




            # with open(file_path, 'r', encoding='utf-8') as f:
                  
            #     data = json.load(f)

            #     count=data["Count"]
            #     data["Emergency"][str(count+1)]["Patient Name"] = patientName
            #     data["Emergency"][str(count+1)]["District"] = district
            #     data["Emergency"][str(count+1)]["Blood Group"] = bloodGroup
            #     data["Emergency"][str(count+1)]["Hospital Name"] = hospitalName
            #     data["Emergency"][str(count+1)]["Contact No"] = cotactNumber
            #     data["Count"] = data["Count"]+1
                
            #     print("--------------------------------------------------------------------------------------------------------------------------------------------------------------")
            #     print(f"{Fore.YELLOW}Your details has been registered... {Fore.CYAN}Patient-Name:{patientName},Blood Group:{bloodGroup},Mobile No.{cotactNumber}, District:{district},Hospital Name:{hospitalName}{Style.RESET_ALL}")
            #     print("--------------------------------------------------------------------------------------------------------------------------------------------------------------")
           
            # with open(file_path, 'w') as f:
            #     json.dump(data, f, indent=4)
        file_path = "Database.json"
        load_json(file_path)
#----------------------------------------------------------------------------------------------------
    def deleteEmergencyDetails():
        
            cotactNumber= input("Enter the Contact Number of the patient: ")
            patientName = input("Enter the Patient Name: ")
            #MYSQL DB
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Vikkramvikky#0821',
                database='BloodDonors'
                )
    
            cursor = connection.cursor()
            
            delete_query = "DELETE FROM Emergency WHERE ContactNo = %s OR PatientName = %s"
            cursor.execute(delete_query,(cotactNumber,patientName))
            
            connection.commit()
            
            
            cursor.close()
            connection.close()
#----------------------------------------------------------------------------------------------------

    
    

    i=1
    while (i>0):
        print(Fore.RED+"-----------------------------------------------------------")
        print(f" {Fore.WHITE}Ask your query ---->"+Style.RESET_ALL+"\n\n"+Fore.BLUE+" 1.Register your Blood Group Detail.\n 2.List of people in particular District with required Blood. \n 3.Required Blood in all District. \n 4.Blood Match.(Options of blood) \n 5.Show all the list in particular District.\n 6.Emergency Details  \n 7.Update Emergency Details\n 8.Delete Patient\n 9.Exit")  
        print(Fore.RED+"-----------------------------------------------------------")
        n = int(input(Fore.BLACK+"Enter the number(1-5)---> "+Style.RESET_ALL))
        if(n==1):
            registerAccount()
        elif (n==2):
            bloodInCity()
        elif(n==3):
            bloodInAllCities()
        elif(n==4):
            bloodMatch()
        elif(n==5):
            showAllInCity()
        elif(n==6):
            displayInfo()
        elif(n==7):
            updateEmergencyDetaisl()
        elif(n==8):
            deleteEmergencyDetails()
        elif(n==9):
            i=0
        else:
             print("You have entered wrong number")

#Calling Main Class.
Main()





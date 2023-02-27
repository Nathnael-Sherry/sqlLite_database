from main import Travellers

try:
    traveller_name = input("Enter your name \n")
    traveller_email = input("Enter your email \n")
    traveller_phonenumber = input("Enter your phonenumber \n")
    traveller_county = input("Enter your county \n")
    traveller_religion = input("Enter your religion \n")
    traveller_gender = input("Enter your gender \n")
    traveller_password = input("Enter your password \n")

    Travellers.create(name=traveller_name, email=traveller_email, password=traveller_password,
                      phonenumber=traveller_phonenumber, county=traveller_county, religion=traveller_religion,
                      gender=traveller_gender)
    print("Traveller Registered Successfully")


except:
    print("Failed to Register Traveller Use a Different Email")

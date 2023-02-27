from main import Travellers

mytravellers = Travellers.select()
for traveller in mytravellers:
    print(traveller.name, traveller.phonenumber, traveller.email, traveller.county, traveller.gender, traveller.religion, traveller.password)
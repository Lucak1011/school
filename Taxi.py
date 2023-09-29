from threading import local


print("Hello, enter the distance you are travelling and the amount of passengers to get a price") 

'''Variables'''

Pax = int(input("How many passengers are there?"))
Dist = int(input("How far are you travelling?"))
Local = input("Is your job local. Answer with yes or no")
'''End of variables
'''
if Local == "no":
    print("You are now being charged a fixed price")
    Dest = input("Where are you going?")
    if Dest == "London":
        Paxprice = Pax * 4
        Fixed = 150
        Nationaltotal = Paxprice + Fixed
        print(Nationaltotal)
        exit()
    if Dest == "Manchester":
        Paxprice = Pax * 5
        Fixed = 125
        Nationaltotal = Paxprice + Fixed
        print(Nationaltotal)
        exit()


PaxPri = Pax * 2
DistPrice = Dist * 1.5

Total = DistPrice + PaxPrice
print(Total)

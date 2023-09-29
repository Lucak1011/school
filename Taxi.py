from threading import local


print("Hello, enter the distance you are travelling and the amount of passengers to get a price") 

Pax = int(input("How many passengers are there?"))
Dist = int(input("How far are you travelling?"))
Local = input("Is your job local. Answer with yes or no")

if (Local == "no"):
    print("You are now being charged a fixed price")
    Dest = input("Where are you going?")
    if (Dest == "London"): 
        Pax = Pax * 4
        Fixed = 150
        Total1 = Pax + Fixed
        print(Total1)


PaxPrice = Pax * 2
DistPrice = Dist * 1.5

Total = DistPrice + PaxPrice
print(Total)

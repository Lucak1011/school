print("Hello, enter the distance you are travelling and the amount of passengers to get a price") 

Pax = int(input("How many passengers are there?"))
Dist = int(input("How far are you travelling?"))

PaxPrice = Pax * 2
DistPrice = Dist * 1.5

Total = DistPrice + PaxPrice
print(Total)

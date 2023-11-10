running = True
while running == True:
    #variables
    funct = input("Enter function")
    
    if funct == "deal checker":
        
        sale_price = int(input("Enter the sale price"))
        original_price = int(input("Enter the original price"))

        if sale_price < original_price:
            print("You got a good offer")
            print((sale_price / (original_price - sale_price)*100))
        elif sale_price > original_price:
            print("you didn't get a deal")
        elif sale_price == original_price:
            print("You paid the same amount")
                  
        

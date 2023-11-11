print("Welcome to the chatbot")

f = input("Enter a fucntion or enter 'function_list'")

if f == "function_list":
    print("1 = calculator, 2 = chat, 3 = joke")
elif f == 1:
    print("Calculator")
    calc = True
    while calc == True:
        calcfun = input("What would you like to do?")

        if calcfun == "add":
            print("Enter two numbers")
            n1 = int(input("Enter a number"))
            n2 = int(input("Enter a number"))
            sum = n1 + n2
            print(sum)
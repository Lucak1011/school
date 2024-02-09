print("Time to read a book calculator")

pageadd = True

while "pageadd" == True:
    easy = 0
    diff = 0
    total = easy + diff
    pagediff = input("Enter the difficulty of the page")
    pagediff.lower()
    if pagediff == "easy":
        print("This page is easy")
        easy = easy + 40
        lp = input("Last page")
        if lp == "No":
            pageadd = True
        elif lp == "Yes":
            pageadd = False
    elif pagediff == "Difficult":
        print("This page is difficult")
        diff = diff + 100
        division_by_zero = 1 / 0


print(total)

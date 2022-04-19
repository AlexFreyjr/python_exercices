#command line calculator

def calculator(nbr1,nbr2,operator) :
    if (operator == '+') :
        result = nbr1 + nbr2
        print(result)

    elif (operator == '-') :
        result = nbr1 - nbr2
        print(result)

    elif (operator == '*') :
        result = nbr1 * nbr2
        print(result)

    elif (operator == '/') :
        result = nbr1 / nbr2
        print(result)
    else:
        print("operator not recognised, please use simple operator like : +,-,* or /")


def main(): 
    while True:
        print("Python command line calculator")
        nbr1 = input("Enter a number : ")
        nbr2 = input("Enter a second number : ")
        nbr_operator = input("Enter the operator : ")
        if nbr1 == "exit" or nbr2 == "exit" or nbr_operator == "exit":
            return False
        else:
            try:
                nbr1 = int(nbr1)
                nbr2 = int(nbr2)
                calculator(nbr1,nbr2,nbr_operator)
            except ValueError:
                print("numbers only")

main()
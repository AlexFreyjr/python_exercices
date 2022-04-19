"""
pseudo code :
ask for start number
take nbr
while nbr > 1
    if nbr modulo 2 = 0 
        then it's even
        return nbr/2
    else 
        return (nbr * 3) + 1 
"""

def calc_algo(nbr):
    i = 0
    while nbr > 1 :
        i+=1
        print(nbr)
        print(i)
        if (nbr % 2) == 0 :
            nbr = nbr / 2
            print(nbr)
        else: 
            nbr = (nbr * 3) + 1
            print(nbr)

    print(f"it has take {i} iteration to reach 1")

def main():
    nbr = input("Please choose a number: ")
    try: 
        nbr = int(nbr)
        calc_algo(nbr)
    except ValueError:
        print("Please enter only numbers")

print("Syracuse Suite calculator")
main()

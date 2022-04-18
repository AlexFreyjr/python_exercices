from math import pi

def PyFinder(num): 
    if num >= 15 :
        print("nope")
    else :
        print(pi)



    
num = input('Input a number between 1 and 15 : ')
int_nbr = int(num)
PyFinder(int_nbr)
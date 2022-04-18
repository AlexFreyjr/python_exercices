from math import pi

def PyFinder(num): 
    if num >= 15 :
        print("Only numbers between 1 and 15")
    else :
        print(pi)
    
num = input('Input a number between 1 and 15 : ')
try:
    int_nbr = int(num)
    PyFinder(int_nbr)
except:
    print("Only numbers please")
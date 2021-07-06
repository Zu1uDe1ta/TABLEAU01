#   Name: Chris Chavez
#   Date: 06 JULY 2021
#   Class: CMPSC 132
#   Description: Quadratic Formula calculator.

import math 

try:
  print("Enter three real numbers for quadratic formula calculation. \n")
  a = int(input("Please input 1st real number: \n"))
  b = int(input("Enter 2nd real number: \n"))
  c = int(input("Now enter the 3rd real number: \n"))
except Exception:
  print("You did not enter a real number, please try again.")


def equationroots(): 
    global a, b, c
    # calculating discriminant using formula
    dis = b * b - 4 * a * c 
    sqrt_val = math.sqrt(abs(dis)) 
      
    # checking condition for discriminant
    if dis > 0: 
        print("\nreal and different roots ") 
        print((-b + sqrt_val)/(2 * a)) 
        print((-b - sqrt_val)/(2 * a)) 
      
    elif dis == 0: 
        print("\nreal and same roots") 
        print(-b / (2 * a)) 
      
    # when discriminant is less than 0
    else:
        print("\nComplex Roots") 
        print(- b / (2 * a), " + i", sqrt_val) 
        print(- b / (2 * a), " - i", sqrt_val) 

"""" 
# Driver Program 
a = 2
b = -10
c = 0
"""

# If a is 0, then incorrect equation
if a == 0: 
        print("\nInput correct quadratic equation") 
  
else:
    equationroots()


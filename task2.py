# Task 2: Using the Math Module for Calculations
 
# Problem Statement: Write a Python program that:
# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
# o   Square root of the number
# o   Natural logarithm (log base e) of the number
# o   Sine of the number (in radians)
# 3.   Displays the calculated results.


import math
def number():
    n=float(input("Enter a number : "))
    
    square_root= math.sqrt(n)
    natural_log= math.log(n)
    sine_value= math.sin(n)
    
    print("Square root ",n," : ",square_root)
    print ( "Logarithm ",n," : ",natural_log)
    print( "sine : ",n," : ",sine_value)

number()

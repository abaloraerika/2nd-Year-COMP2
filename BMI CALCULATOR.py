# -*- coding: utf-8 -*-
"""
Created on Sat May 11 10:29:20 2024

@author: abalo
"""

# -*- coding: utf-8 -*-
"""
Created on Sat May 11 10:29:20 2024
@author: abalo
"""

print("Welcome to the BMI Calculator!")
weight = 1
height = 0
bmi = 0
while weight != 0 or height != 0:
    weight = eval(input("Enter your weight in kilograms: "))
    if weight == 0:
        print("Program Terminated")
        break
    else:
        height = eval(input("Enter your height in meters: "))
        if height == 0:
            print("Program Terminated")
            break
        else:
            bmi = weight / (height ** 2)
            print("Your BMI is:", bmi)
            if bmi < 18.5:
                print("You are classified as underweight")
            elif 18.5 <= bmi < 25:
                print("You are classified as normal weight")
            elif 25 <= bmi < 30:
                print("You are classified as overweight")
            elif bmi >= 30:
                print("You are classified as obese")

print("Thank you for using the BMI Calculator!")

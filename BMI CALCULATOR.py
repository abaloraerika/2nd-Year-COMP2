# -*- coding: utf-8 -*-
"""
Created on Sat May 11 10:29:20 2024

@author: abalo
"""

print("Welcome to the BMI Calculator!")
weight=1
height=0
bmi=0
while weight!=0 or height!=0:
    weight=eval(input("Enter your weight in kilograms: "))
    if weight ==0:
        print("Program Terminated")
        break
    else:
        height=eval(input("Enter your height in meters: "))
        if height==0:
            print("Program Terminated")
            break
        else:
            bmi=weight/(height**2)
            print("Your BMI is: ", bmi)
            if  bmi<18.5:
                print("You are classified as underweight")
            elif bmi>=18.5 and bmi<=24.9:
                print("You are classified as normal weight")
            elif bmi>=25 and bmi==29.9:
                print("You are classified as overweight")
            if bmi>30:
                print("You are classified as obese")

print("Thank you for using the BMI Calculator!")
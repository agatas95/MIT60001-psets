#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 12:32:26 2019

@author: chananyajacobson
"""

print("Let's figure out if you can save up for a down payment within three years.")

r = 0.04
total_cost = 1000000
semi_annual_raise = 0.07
down_payment = total_cost * 0.25
set_annual_salary =  float(input("Okay, how much are you making a year? "))
min_portion_saved = 0
max_portion_saved = 10000

num_steps = 0
current_savings = 0
guess = 5000

    
while abs(down_payment - current_savings) >= 100:
         
    guess = (max_portion_saved + min_portion_saved) // 2 
    months = 0
    current_savings = 0
    annual_salary = set_annual_salary

    while months < 36:
        current_savings += current_savings * r / 12
        current_savings += annual_salary / 12 * guess / 10000
        if months > 0 and months % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
        months += 1

    if current_savings < down_payment:
            min_portion_saved = guess
    else:
            max_portion_saved = guess
            
   
    num_steps += 1
    
    if guess >= 9999 and current_savings < down_payment:
        print("It is not possible to pay the down payment in three years on this salary.")
        break
if abs(down_payment - current_savings) <= 100:
    print("Best savings rate: ", guess / 10000)
    print("Steps in the bisection search: ", num_steps)    
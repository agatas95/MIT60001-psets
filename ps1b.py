#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 12:03:11 2019

@author: chananyajacobson
"""
print("Let's figure out how long it will take you to buy your dream house.")
current_savings = 0
r = 0.04
annual_salary = float(input("Okay, how much are you making a year? "))
portion_saved = float(input("What percent of your salary are you willing to save each month? ")) / 100
total_cost = float(input("How much does your dream house cost? "))
semi_annual_raise = float(input("What percent raise do you think you will get semi-annually? ")) / 100
portion_down_payment = total_cost * 0.25

months = 0

while current_savings < portion_down_payment:
    current_savings += current_savings * r / 12
    current_savings += annual_salary / 12 * portion_saved
    if months > 0 and months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
    months += 1
    
print("At this rate, it will take you", months, "months to save up for a down payment.")
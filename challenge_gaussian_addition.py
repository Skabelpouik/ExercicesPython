# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 10:02:08 2021

@author: Peridot
"""

# Gaussian Addition
def gauss_addition(number_list):
    sum_numbers = 0
    count_iteration = 0
    while len(number_list):
        first_number = number_list.pop(0)
        last_number = number_list.pop(-1)
        sum_numbers += first_number + last_number
        print("The current numbers are %d and %d. The partial sum is %d" % (first_number, last_number, sum_numbers))
        count_iteration += 1
    print("There were %d partial sums." % count_iteration)

        
gauss_addition(list(range(1, 101)))
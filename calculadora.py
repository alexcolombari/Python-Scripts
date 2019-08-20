#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author: Alex Colombari (http://github.com/alexcolombari)
Date: 2019-08-20

Available functions:

+ : addition
- : subtraction
* : multiplication
/ : division
% : percentage

"""

import sys

def calculator(input_term):
    """
    This is the man function
    output --> returns the output input_term
    """

    # Converting input input_terms
    input_term = input_term.replace(' ', '')
    input_term = input_term.replace('=', '')
    input_term = input_term.replace('?', '')
    input_term = input_term.replace('^', '**')
    input_term = input_term.replace('%', '/100.00')

    try:
        input_term = eval(input_term)
    except ZeroDivisionError:
        print("Can't divide by 0. Try again.")
    except NameError:
        print("Invalid input")
    except TypeError:
        print("Enter inputs of correct datatype")
    
    return input_term

def result(input_term):
    print("\n" + str(calculator(input_term)) + "\n")

def main():
    print("welcome to calculator - Enter quit to exit")

    if sys.version_info.major >= 3:
        while True:
            i = input("Do your operations: ")
            if i == 'quit':
                break
            result(i)

    else:
        while True:
            i = raw_input("Do your operations: ")
            if i == 'quit':
                break
            result(i)

if __name__ == '__main__':
    main()

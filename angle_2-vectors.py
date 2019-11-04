#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
	Python program to find the angle between two vectors
	Author: Alex Colombari -> www.github.com/alexcolombari
	Date: 10-04-2019
'''

import os
import numpy as np
import matplotlib.pyplot as plt

def clear_screen():
	return os.system("cls" if os.name == "nt" else "clear")

def dotproduct(vetor1, vetor2):
	x = (np.dot(vetor1[0], vetor2[0]) + np.dot(vetor1[1], vetor2[1]) + np.dot(vetor1[2], vetor2[2]))
	return x

def raiz(vetor1, vetor2):
	raiz1 = np.sqrt((vetor1[0] ** 2) + (vetor1[1] ** 2) + (vetor1[2] ** 2))
	raiz2 = np.sqrt((vetor2[0] ** 2) + (vetor2[1] ** 2) + (vetor2[2] ** 2))
	return raiz1 * raiz2

def angle_between(x, y):
	divisao = x / y
	return np.arccos(divisao)


if __name__ == "__main__":

	clear_screen()

	v1 = input("Value of X1: ")
	v2 = input("Value of Y1: ")
	v3 = input("Value of Z1: ")

	u1 = input("\nValue of X2: ")
	u2 = input("Value of Y2: ")
	u3 = input("Value of Z2: ")

	vetor1 = np.array([v1,v2,v3])
	vetor2 = np.array([u1,u2,u3])

	x = dotproduct(vetor1, vetor2)
	y = raiz(vetor1, vetor2)
	xy = angle_between(x, y)

	print("\nResult between two vectors: {:.2f}".format(xy))


'''	
	Resultado:
	se foi > 0 é entre 0 e 90
	se foi = 0 é 90
	se foi < 0 é entre 90 e 180
'''

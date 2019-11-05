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
	# return os.system("cls" if os.name == "nt" else "clear")
	return os.system("clear" if os.name == "posix" else "cls")

def dotproduct(vetor1, vetor2):
	return np.dot(vetor1[0], vetor2[0]) + np.dot(vetor1[1], vetor2[1]) + np.dot(vetor1[2], vetor2[2])

def squared_root(x):
	return x ** (1.0 / 2)

def raiz(vetor1, vetor2):
	raiz1 = squared_root((vetor1[0] ** 2) + (vetor1[1] ** 2) + (vetor1[2] ** 2))
	raiz2 = squared_root((vetor2[0] ** 2) + (vetor2[1] ** 2) + (vetor2[2] ** 2))
	return raiz1 * raiz2

def angle_between(x, y):
	return np.arccos(x / y)

def main():
	clear_screen()

	print("┌──────────────────────────────────────┐")
	print("│                                      │")
	print("│      Angle between two vectors       │")
	print("│                                      │")
	print("└──────────────────────────────────────┘")

	v1 = input("\n             x1 value: ")
	v2 = input("             y1 value: ")
	v3 = input("             z1 value: ")

	u1 = input("\n             x2 value: ")
	u2 = input("             y2 value: ")
	u3 = input("             z2 value: ")

	vetor1 = np.array([v1,v2,v3])
	vetor2 = np.array([u1,u2,u3])

	x = dotproduct(vetor1, vetor2)
	y = raiz(vetor1, vetor2)
	xy = angle_between(x, y)

	print("\n┌──────────────────────────────────────┐")
	print("│  Result between two vectors = {:.2f}   │".format(xy))
	print("└──────────────────────────────────────┘")


if __name__ == "__main__":
	main()

'''	
	Resultado:
	se foi > 0 é entre 0 e 90
	se foi = 0 é 90
	se foi < 0 é entre 90 e 180
'''

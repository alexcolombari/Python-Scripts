'''
	Memory stress test using Python
	Author: Alex Colombari (https://github.com/alexcolombari)
	Date: 11-11-2019
'''
import os, sys
import time

try:
	import psutil
except:
	os.system("pip install psutil")

# print(psutil.virtual_memory())
print("\nThe program stops when exceed the maximum memory usage you will define below, press any button and press Enter to start...")

inp = (raw_input()if sys.version_info[0] < 3 else input())

if inp:
	maximum_memory = int(input("Enter the maxium memory to use (in percentage): "))
	initial_time = time.time()
	number = 2
	print("\nInitial memory usage: {}%".format(psutil.virtual_memory()[2]))
	while True:
		try:
			if psutil.virtual_memory()[2] <= maximum_memory:
			    number = number ** 2
			    print("Memory usage: {}% || CPU usage: {}%".format(psutil.virtual_memory()[2], psutil.cpu_percent()))
			    time.sleep(0.05)
			else:
				print("\nAvailable memory exceeded!")
				print("Elapsed time: {:.2f} seconds".format(time.time() - initial_time))
				break
		except KeyboardInterrupt:
			print("\nProgram finished!")
			break	

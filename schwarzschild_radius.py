'''
	Schwarzschild Radius appication
	Author: Alex Colombari (http://github.com/alexcolombari)
	Date: 11-08-2019

	References:
	http://astro.if.ufrgs.br/evol/node53.htm   (in portuguese)
	http://astronomy.swin.edu.au/cosmos/S/Schwarzschild+Radius   (in english)
'''

class Schwarzschild:
	def __init__(self, mass):
		self.mass = mass

	def formula(self):
		gravity_constant = 6.67 * 10**-11
		light_velocity = 299792458 # 299 792 458 m/s

		schwarzschild = (((2 * gravity_constant) * self.mass) / (light_velocity ** 2))

		return schwarzschild

if __name__ == "__main__":
	inp = input("Enter with your mass: ")
	schwarz = Schwarzschild(inp)
	print("Schwarzschild Radius = {}".format(schwarz.formula()))

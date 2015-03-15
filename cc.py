#!/usr/bin/env python

def calc_corrected_ca(serum_ca, serum_albumin):
	"""Calculates Calcium corrected for Hypoalbuminemia"""
	normal_albumin = 4 #normal albumin in mg/dL
	return (0.8*(normal_albumin-serum_albumin))+serum_ca

def get_float(prompt):
	while True:
		try:
			value = float(raw_input(prompt))
		except ValueError:
			print "Please enter a number."
		except KeyboardInterrupt:
			print "\n"
			exit(0)
		else:
			return value
			break

def main():
	print "\nCalcium Correction for Hypoalbuminemia"
	print "--------------------------------------"

	print "Corrected Calcium = " + str(calc_corrected_ca(get_float("Serum Calcium (mg/dL): "), get_float("Serum Albumin (mg/dL): "))) + " mg/dL\n"

if __name__ == "__main__" : main()
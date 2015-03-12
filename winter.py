#!/usr/bin/env python

def calc_winter(hco3):
	"""Calculates Winter's Formula
	
	Returns tuple with minimum and maximum value of expected PCO2 compensation for metabolic acidosis
	"""
	expected_pco2 = 1.5*hco3+8
	return (expected_pco2-2, expected_pco2+2)

def get_hco3():
	while True:	
		try:
			hco3 = float(raw_input("Bicarbonate (mEq/L): "))
		except ValueError:
			print "Please enter a number."
		except KeyboardInterrupt:
			exit(0)
		else:
			if hco3 > 0:
				return hco3
				break
			else:
				print "Value must be greater than 0."

def main():
	print "\nWinter's Formula for Metabolic Acidosis Compensation"
	print "----------------------------------------------------"
	
	expected_pco2_range = calc_winter(get_hco3())

	print "Expected PCO2 Compensation: " + str(expected_pco2_range[0]) + "-" + str(expected_pco2_range[1]) + "\n"


if __name__ == "__main__": main()
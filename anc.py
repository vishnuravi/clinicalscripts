#!/usr/bin/env python

def calc_anc(wbc, pmn, bands):
	"""Calculates Absolute Neutrophil Count"""
	return 10*wbc*(pmn+bands)

def get_float(min, prompt):
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


def main():
	print "\nAbsolute Neutrophil Count"
	print "-----------------------------"
	wbc = get_float(0, "WBC Count (in 1000s): ")
	pmn = get_float(0, "Percent Segmented Neutrophils (%): ")
	bands = get_float(0, "Percent Bands (%): ")
	anc = calc_anc(wbc, pmn, bands)
	print "\nAbsolute Neutrophil Count is " + str(anc) + " x 10^3/uL\n"


if __name__ == "__main__": main()
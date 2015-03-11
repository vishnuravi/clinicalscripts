#!/usr/bin/env python

def calc_anion_gap(na, cl, hco3):
	"""Calculate Anion Gap"""
	return na-(cl+hco3)

def calc_delta_gap(ag):
	"""Calculate Delta Gap"""
	return ag-12.0

def calc_delta_ratio(ag, hco3):
	"""Calculate Delta Ratio"""
	return (ag-12.0)/(24.0-hco3)

def get_na():
	while True:	
		try:
			na = float(raw_input("Sodium (mEq/L): "))
		except ValueError:
			print "Please enter a number."
		else:
			if 80.0 <= na <= 200.0:
				return na
				break
			else:
				print "Value must be between 80.0 and 200.0 mEq/L."

def get_cl():
	while True:	
		try:
			cl = float(raw_input("Chloride (mEq/L): "))
		except ValueError:
			print "Please enter a number."
		else:
			if 60.0 <= cl <= 180.0:
				return cl
				break
			else:
				print "Value must be between 60.0 and 180.0 mEq/L."

def get_hco3():
	while True:	
		try:
			hco3 = float(raw_input("Bicarbonate (mEq/L): "))
		except ValueError:
			print "Please enter a number."
		else:
			return hco3
			break

def main():
	print "\nAnion Gap Calculator"
	print "---------------------------"
	na = get_na()
	cl = get_cl()
	hco3 = get_hco3()
	print "---------------------------"

	anion_gap = calc_anion_gap(na, cl, hco3)
	delta_gap = calc_delta_gap(anion_gap)
	delta_ratio = calc_delta_ratio(anion_gap, hco3)

	print "\nResults"
	print "---------------------------"
	print "Anion Gap: " + str(anion_gap) + " mEq/L"
	print "Delta Gap: " + str(delta_gap) + " mEq/L"
	print "Delta Ratio: " + str(delta_ratio) + " mEq/L"


if __name__ == "__main__": main()
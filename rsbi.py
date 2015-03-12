#!/usr/bin/env python

def calc_rsbi(resp_rate, tidal_volume):
	"""Calculates Rapid Shallow Breathing Index"""
	return resp_rate/tidal_volume

def get_float(min, prompt):
	while True:
		try:
			value = float(raw_input(prompt))
		except ValueError:
			print "Please enter a number."
		except KeyboardInterrupt:
			exit(0)
		else:
			if value > min:
				return value
				break
			else:
				print "Value must be greater than 0."


def main():
	print "\nRapid Shallow Breathing Index"
	print "-----------------------------"
	resp_rate = get_float(0, "Patient's Respiratory Rate (breaths/min): ")
	tidal_volume = get_float(0, "Patient's Tidal Volume (L): ")
	score = calc_rsbi(resp_rate, tidal_volume)
	print "\nRapid Shallow Breathing Index is " + str(score) + " breaths/min/L"

	if(score <= 105):
		print "\nA score <= 105 generally indicates readiness for weaning.\n"
	else:
		print "\nA score > 105 indicates a high probability of weaning failure and re-intubation.\n"



if __name__ == "__main__": main()
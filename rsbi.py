def rsbi(f, vt):
	"""Calculate Rapid Shallow Breathing Index"""
	return f/vt


def main():
	print "Rapid Shallow Breathing Index = Respiratory Rate/Tidal Volume"
	f = input('Patient\'s Respiratory Rate (breaths/min): ')
	vt = input('Patient\'s Tidal Volume (L): ')
	score = rsbi(f, vt)
	print "Rapid Shallow Breathing Index is " + str(score) + " breaths/min/L"

	if(score <= 105):
		print "A score <= 105 generally indicates readiness for weaning."
	else:
		print "A score > 105 indicates a high probability of weaning failure and re-intubation."



if __name__ == "__main__": main()
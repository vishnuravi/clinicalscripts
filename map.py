#!/usr/bin/env python
""" Calculates Mean Arterial Pressure (MAP)

MAP = ((1/3)*Systolic Blood Pressure) + ((2/3)*Diastolic Blood Pressure)

A MAP >= 60 mmHg is thought to be needed to maintain adequate tissue perfusion.

"""

def calc_map(sbp, dbp):
	return (1.0/3.0*sbp)+(2.0/3.0*dbp)

def get_float(prompt, min=0):
    while True:
        try:
            value = float(raw_input(prompt))
        except ValueError:
            print "Please enter a number."
        except KeyboardInterrupt:
            exit(0)
        else:
            if value < min:
                print "This value cannot be less than {}.".format(min)
            else:
                return value
def main():
	print "Mean Arterial Pressure"
	print "----------------------"
	sbp = get_float("Systolic Blood Pressure (mm Hg): ")
	dbp = get_float("Diastolic Blood Pressure (mm Hg): ")
	print "\nMean Arterial Pressure: {} mm Hg".format(int(calc_map(sbp, dbp)))

if __name__ == '__main__':
	main()
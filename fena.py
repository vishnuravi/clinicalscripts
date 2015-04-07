#!/usr/bin/env python
""" Calculates the fractional excretion of sodium """

def calc_fena(p_na, p_cr, u_na, u_cr):
	return (u_na*p_cr)/(p_na*u_cr)*100

def get_float(prompt, min=0):
    while True:
        try:
            value = float(raw_input(prompt))
        except ValueError:
            print "Please enter a number."
        except KeyboardInterrupt:
            print "\n"
            exit(0)
        else:
            if value < min:
                print "This value cannot be less than {}.".format(min)
            else:
                return value

def main():
	print "Fractional Excretion of Sodium"
	print "------------------------------"
	p_na = get_float("Plasma Sodium (mEq/L): ")
	p_cr = get_float("Plasma Creatinine (mg/dL): ")
	u_na = get_float("Urine Sodium (mEq/L): ")
	u_cr = get_float("Urine Creatinine (mg/dL): ")
	fena = calc_fena(p_na, p_cr, u_na, u_cr)
	print "\nFENa is {0:.2f}%.".format(fena)

if __name__ == '__main__':
	main()
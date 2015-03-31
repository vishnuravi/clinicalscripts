#!/usr/bin/env python
""" Uses Light's criteria for exudative effusions to determine if pleural fluid is exudative 

Light's criteria specifies that an exudative effusion will have at least one of the following:

- Pleural Fluid Protein / Serum Protein > 0.5
- Pleural Fluid LDH / Serum LDH > 0.6
- Pleural Fluid LDH > 2/3 of the upper limit of normal serum LDH

"""
from __future__ import division
import sys

def get_float(prompt, min=0):
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
                print "Value must be greater than {}.".format(min)


def main():
    print "\nLight's Criteria for Exudative Effusions"
    print "----------------------------------------"
    serum_protein = get_float("Serum Protein (g/dL): ")
    pleural_protein = get_float("Pleural Fluid Protein (g/dL): ")
    serum_ldh = get_float("Serum LDH (U/L): ")
    pleural_ldh = get_float("Pleural Fluid LDH (U/L): ")
    upper_limit_ldh = get_float("Upper limit of normal serum LDH (U/L): ")
    print "----------------------------------------"

    criteria = 0

    if (pleural_protein/serum_protein) > 0.5:
        print "Effusion protein/serum protein ratio is greater than 0.5."
        criteria += 1

    if (pleural_ldh/serum_ldh) > 0.5:
        print "Effusion LDH/serum LDH ratio is greater than 0.6."
        criteria += 1

    if pleural_ldh > ((2/3)*upper_limit_ldh):
        print "Effusion LDH is greater than two-thirds the upper limit of normal serum LDH."
        criteria += 1

    if criteria >= 1:
        print "{} of Light's criteria have been met - Fluid is likely exudate.".format(criteria)
    else:
        print "None of Light's criteria have been met - Fluid is not likely exudate."

if __name__ == '__main__':
    main()
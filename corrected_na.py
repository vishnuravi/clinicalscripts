#!/usr/bin/env python
""" Calculates a corrected sodium level for hyperglycemia """

def katz(serum_na, serum_glucose):
    """Calculates Sodium corrected for Hyperglycemia using Katz formula"""
    return serum_na + 0.016*(serum_glucose-100)

def hillier(serum_na, serum_glucose):
    """Calculates Sodium corrected for Hyperglycemia using Hillier formula"""
    return serum_na + 0.024*(serum_glucose-100)


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
    print "Calcium Correction for Hypoalbuminemia"
    print "--------------------------------------"
    sodium = get_float("Sodium (mEq/L): ")
    glucose = get_float("Glucose (mg/dL): ")
    print "Corrected Sodium (Katz Formula): {} mEq/L".format(katz(sodium, glucose))
    print "Corrected Sodium (Hillier Formula): {} mEq/L".format(hillier(sodium, glucose))
    
if __name__ == "__main__" : main()
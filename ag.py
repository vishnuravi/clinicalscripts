#!/usr/bin/env python
""" Calculates the anion gap, delta gap, and delta ratio """

def calc_anion_gap(na, cl, hco3):
    """Calculate Anion Gap"""
    return na-(cl+hco3)

def calc_delta_gap(ag):
    """Calculate Delta Gap"""
    return ag-12.0

def calc_delta_ratio(ag, hco3):
    """Calculate Delta Ratio"""
    return (ag-12.0)/(24.0-hco3)

def get_float(min, max, prompt):
    while True:
        try:
            value = float(raw_input(prompt))
        except ValueError:
            print "Please enter a number."
        except KeyboardInterrupt:
            print "\n"
            exit(0)
        else:
            if min <= value <= max:
                return value
                break
            else:
                print "Value must be between {0} and {1}.".format(min, max)


def main():
    print "\nAnion Gap Calculator", "\n---------------------------"
    na = get_float(80, 200, "Sodium (mEq/L): ")
    cl = get_float(60, 180, "Chloride (mEq/L): ")
    hco3 = get_float(0, 60, "Bicarbonate (mEq/L): ")

    anion_gap = calc_anion_gap(na, cl, hco3)
    delta_gap = calc_delta_gap(anion_gap)
    delta_ratio = calc_delta_ratio(anion_gap, hco3)

    print "\nResults", "\n---------------------------"
    print "Anion Gap: {} mEq/L".format(anion_gap)
    print "Delta Gap: {} mEq/L".format(delta_gap)
    print "Delta Ratio: {} mEq/L".format(delta_ratio)


if __name__ == "__main__": main()
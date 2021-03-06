#!/usr/bin/env python
""" Calculates the Absolute Neutrophil Count """

def calc_anc(wbc, pmn, bands):
    return 10*wbc*(pmn+bands)

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

def get_percent(prompt):
    while True:
        try:
            value = float(raw_input(prompt))
        except ValueError:
            print "Please enter a number."
        except KeyboardInterrupt:
            print "\n"
            exit(0)
        else:
            if value < 0:
                print "This value cannot be less than 0."
            elif value > 100:
                print "This value cannot be more than 100."
            else:
                return value

def neutropenia_category(anc):
    if anc < 500:
        neutropenia = "Severe Neutropenia"
    elif anc < 1000:
        neutropenia = "Moderate Neutropenia"
    elif anc < 1500:
        neutropenia = "Mild Neutropenia"
    else:
        neutropenia = "No Neutropenia"
    
    return neutropenia

def main():
    print "\nAbsolute Neutrophil Count", "\n-----------------------------"
    wbc = get_float("WBC Count (in 1000s): ")
    pmn = get_percent("Percent Segmented Neutrophils (%): ")
    bands = get_percent("Percent Bands (%): ")
    anc = calc_anc(wbc, pmn, bands)
    print "\nAbsolute Neutrophil Count is {} x 10^3/uL ({}) \n".format(str(anc), neutropenia_category(anc)) 

if __name__ == "__main__": main()
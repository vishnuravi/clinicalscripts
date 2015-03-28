#!/usr/bin/env python
""" Calculates the serum-ascites albumin gradient to determine the cause of ascites """

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
            if value > min:
                return value
                break
            else:
                print "Value must be greater than {}.".format(min)

def main():
    print "\nSerum-Ascites Albumin Gradient"
    print "------------------------------"
    serum_albumin = get_float("Serum albumin (g/dL): ")
    ascitic_albumin = get_float("Ascitic fluid albumin (g/dL): ")
    saag = serum_albumin - ascitic_albumin

    print "\nSAAG: " + str(saag)
    
    if saag >= 1.1:
        print "High SAAG (> 1.1 g/dL) indicates that the ascites is likely due to portal hypertension.\n"
    else:
        print "Low SAAG (< 1.1 g/dL) indicates that the ascites is not likely due to portal hypertension.\n"

if __name__ == '__main__':
    main()
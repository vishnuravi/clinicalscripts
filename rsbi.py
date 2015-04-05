#!/usr/bin/env python
""" Calculates the Rapid Shallow Breathing Index """

def calc_rsbi(resp_rate, tidal_volume):
    return resp_rate/tidal_volume

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
    print "\nRapid Shallow Breathing Index"
    print "-----------------------------"
    resp_rate = get_float("Patient's Respiratory Rate (breaths/min): ")
    tidal_volume = get_float("Patient's Tidal Volume (L): ")
    score = calc_rsbi(resp_rate, tidal_volume)
    print "\nRapid Shallow Breathing Index is {} breaths/min/L".format(score)

    if(score <= 105):
        print "\nA score <= 105 generally indicates readiness for weaning.\n"
    else:
        print "\nA score > 105 indicates a high probability of weaning failure and re-intubation.\n"

if __name__ == "__main__": main()
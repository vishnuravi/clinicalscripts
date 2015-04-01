#!/usr/bin/env python

import sys

def get_int(min, max, prompt):
    while True:
        try:
            value = int(raw_input(prompt))
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

def get_score(options):
    print options
    return get_int(1,3, "Choose one: ")-1

def main():
    print "APGAR Score"
    print "-----------"
    
    score = 0

    criteria = ["\nActivity: \n 1. Limp and floppy \n 2. Some extremity flexion \n 3. Active motion", 
    "\nPulse: \n 1. Absent \n 2. Less than 100 BPM \n 3. Greater than or equal to 100 BPM",
    "\nGrimace: \n 1. No response to stimulation \n 2. Grimace on suction or stimulation \n 3. Cry on stimulation",
    "\nAppearance: \n 1. Blue or Pale all over \n 2. Body pink and blue extremities \n 3. Body and extremities pink",
    "\nRespirations: \n 1. Absent \n 2. Weak, irregular or gasping \n 3. Strong cry"]

    score = sum(map(get_score, criteria))

    print "\nThe patient's APGAR Score is {}.".format(score)

if __name__ == '__main__':
    main()

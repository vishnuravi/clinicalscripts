#!/usr/bin/env python

import sys

def ask_yes_no(question, default="no"):
    """Asks the user a yes/no question and returns 1 for yes and 0 for no"""

    valid = {"yes": 1, "y": 1, "no": 0, "n": 0}

    if default is None:
        options = " [yes/no] "
    elif default == "yes":
        options = " [YES/no] "
    elif default == "no":
        options = " [yes/NO] "
    else:
        raise ValueError("invalid default answer: {}".format(default))

    while True:
        sys.stdout.write(question + options)
        user_choice = raw_input().lower()
        if default is not None and user_choice == '':
            return valid[default]
        elif user_choice in valid:
            return valid[user_choice]
        else:
            sys.stdout.write("Please respond either 'yes' or 'no' (or 'y' or 'n').")

def get_pos_int(prompt):
    while True:
        try:
            value = float(raw_input(prompt))
        except ValueError:
            print "Please enter a number."
        else:
            if value > 0:
                return value
            else:
                print "This value must be greater than 0."

def interpret_score(score):
    """Returns suggested management for a given Centor score"""
    if -1 <= score <= 1:
        management = "No antibiotic or throat culture neccessary."
    elif 2 <= score <= 3:
        management = "Should receive a throat culture and treat with antibiotic if culture is positive."  
    elif 4 <= score <= 5:
        management = "Treat empirically with an antibiotic."
    else:
        management = "Centor score must be between -1 and 5."

    return management  

def main():
    """ Estimates the probability of streptococcal pharyngitis """

    print "\nModified Centor Score", "\n-------------------"

    #Calculate original Centor Criteria
    criteria = ["Fever (Temp > 100.4 F)", "No cough", "Exudate or swelling of tonsils", "Tender or swollen anterior cervical lymph nodes"]
    score = sum(map(ask_yes_no, criteria))

    #Add on Modified criteria
    age = get_pos_int("What is the patient's age (years)? ")
    if 3 <= age <= 14:
        score += 1
    if age >= 45:
        score -= 1
 

    print "\nModified Center Score: {0}\nSuggested Management: {1}\n".format(score, interpret_score(score))

if __name__ == '__main__':
    main()



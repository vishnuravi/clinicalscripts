#!/usr/bin/env python

import sys

def ask_yes_no(question, default="no"):
    """Asks the user a yes/no question and scores the answer 1 for yes and 0 for no.

    question is a string, default is the answer returned if the user hits Enter.
    """
    
    valid = {"yes": 1, "y": 1, "no": 0, "n": 0}

    if default is None:
        options = " [yes/no] "
    elif default == "yes":
        options = " [YES/no] "
    elif default == "no":
        options = " [yes/NO] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + options)
        user_choice = raw_input().lower()
        if default is not None and user_choice == '':
            return valid[default]
        elif user_choice in valid:
            return valid[user_choice]
        else:
            sys.stdout.write("Please respond either 'yes' or 'no'.")
    
def score_to_mortality(score):
    """Returns the 30 day mortality rate for the given CURB score"""
    return [0.6, 2.7, 6.8, 14.0, 27.8, 27.8][score]

def interpret_score(score):
    """Returns interpretation of the CURB-65 score as a string"""
    if 0 <= score <= 1:
        interpretation = "Consider treating as an outpatient."
    elif 2 <= score <=3:
        interpretation = "Consider inpatient treatment or outpatient with close followup."
    elif 4 <= score <=5:
        interpretation = "Requires hospitalization, consider admitting to ICU."
    else:
        interpretation = "Invalid score: Must be between 0 and 5."

    return interpretation

def main():
    """ Predicts mortality in community-acquired pneumonia using CURB-65 criteria """

    print "\nCURB-65 Severity Score", "\n----------------------"
    
    criteria = ['Confusion', 'BUN > 19 mg/dL', 'Resp. Rate >= 30', 'Systolic BP < 90 mmHg or Diastolic BP <= 60 mmHg', 'Age >= 65']
    
    score = sum(map(ask_yes_no, criteria))

    print "\nCURB-65 Score: {} \n30-day mortality rate: {}% \n{} \n".format(score, score_to_mortality(score), interpret_score(score))

if __name__ == "__main__": main()
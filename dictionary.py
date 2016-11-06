vocabulary_words = {"tuple": "imutable data structure", "integer": "whole number", "boolean": "True/False"}

def num_times_letter_in_name(name):
    letter_dictionary = {}
    for l in name.lower():
        #fill in dictionary
        if l not in letter_dictionary:
            letter_dictionary[l] = 1
        #give letter
        else:
            letter_dictionary[l] += 1
        #count letter if it is a repeat
    return letter_dictionary

print num_times_letter_in_name("Alais de Hoogh") 

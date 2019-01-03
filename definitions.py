import json
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))
def print_def(word):
    word = word.lower()
    if word not in data:
        print(get_close_matches(word, data.keys())[0])
        # return "no such word"
    else:
        return data[word]
blah = input("Enter a word ")
# print(print_def(blah))  


def describe(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " %get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."    
    else:
        return "The word doesn't exist. Please double check it."    

output = (describe(blah))
if type(output) == list:  
    for item in output:
        print(item)
else:
    print(output)      
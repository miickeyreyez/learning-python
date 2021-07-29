import json
from difflib import get_close_matches

data = json.load(open('dataset/data.json'))

def translate(word):
  word = word.lower()
  title = word.title()
  upper = word.upper()
  closes_matches = get_close_matches(word, data.keys())
  close_match = closes_matches[0] if len(closes_matches) > 0 else []

  if word in data:
    return data[word]
  elif upper in data:
      return data[upper]
  elif title in data:
    return data[title]
  elif len(close_match) > 0:
    yn = input("Did you mean %s instead? Y/N: " % close_match)
    if yn.upper() == 'Y':
        return data[close_match]
    else:
      return "No matches found"
  else:
    return "Non-existent word"

word = input('Enter word: ')

output = translate(word)

if type(output) == list:
  for item in output:
    print(item)
else:
  print(output)
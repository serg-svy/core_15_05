import re

def find_word(text, word):
    match = re.search(word, text, re.IGNORECASE)

    if match:
        index = match.span()
        result = {
            'result': True,
            'first_index': index[0],
            'last_index': index[1],
            'search_string': word,
            'string': text
        }
    else:
        result = {
            'result': False,
            'first_index': None,
            'last_index': None,
            'search_string': word,
            'string': text
        }

    return result


print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "Python"))


phrase = str(input("Enter phrase: "))

# makes string all lowercase and deletes spaces
stripped_phrase = phrase.lower().replace(" ", "")

# uses extended slicing as [begin:end:step], leaving begin and end empty means using full string
reversed_phrase = stripped_phrase[::-1].lower().replace(" ", "")

if stripped_phrase == reversed_phrase:
    print('Phrase is palindrome')
else:
    print('Phrase is not palindrome')

# used for "testing" script
# print(reversed_phrase)
# print(stripped_phrase)

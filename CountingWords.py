
phrase = input("Input a phrase: ")

list_of_words = []

# splits string if " " space is spotted
list_of_words = phrase.split(" ")

count = 0

for i in list_of_words:
    count += 1

print(f'Phrase contains {count} words.')

# "testing" reasons
# print(list_of_words)
# print(count)

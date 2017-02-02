phrase = raw_input("Enter a phrase: ")
if phrase[len(phrase)-1] == "!":
    print phrase.upper()
else:
    print phrase.lower()

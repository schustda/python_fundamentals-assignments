phrase = raw_input("Enter a phrase: ")
newstr = ""
for x in range(len(phrase)):
    if x == 0 or x % 2 == 0:
        newstr += phrase[x].upper()
    else:
        newstr += phrase[x].lower()
print newstr

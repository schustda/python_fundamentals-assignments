phrase = raw_input("Enter a phrase: ")
newstr = phrase
vowels = ('a', 'e', 'i', 'o', 'u')
for x in phrase.lower():
    if x in vowels:
        newstr = newstr.replace(x,"")
print newstr

phrase = raw_input("Enter a phrase: ")
letter = raw_input("Enter a letter: ")
count = 0
for i in phrase:
    if i == letter:
        count += 1
if count == 1:
    print "There is "+str(count)+" of the specified letter in your phrase."
else:
    print "There are "+str(count)+" of the specified letter in your phrase."

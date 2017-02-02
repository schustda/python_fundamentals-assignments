set_A = set([])
loop = 1
while loop == 1:
    x = str(raw_input("Enter a word to add to the vocabulary: "))
    if x == 'v':
        print set_A
    elif x == 'q':
        loop = 0
    else:
        set_A.add(x)

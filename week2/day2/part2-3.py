loop = 1
second_loop = 1
dictionary = {}
while loop == 1:
    x = raw_input("Please enter a coordinate-word pair in the format (x, y, word): ")
    if str(x) == "":
        loop = 0
        break
    else:
        x = x.split(",")
        dictionary[(int(x[0]),int(x[1]))] = str(x[2])
while second_loop == 1:
    y = raw_input("Please enter a coordinate to look up: ")
    if y == 'q':
        second_loop = 0
        break
    else:
        z = 0
        y = y.split(",")
        for (a,b) in dictionary:
            if a == int(y[0]) and b == int(y[1]):
                p = dictionary[(a,b)]
                z = 1
                break
        if z == 1:
            print p
        else:
            print "Coortinates not found"

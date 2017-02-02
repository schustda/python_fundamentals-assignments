#part 2-1
def word_counter(x):
    return len(x.split())

#part 2-2
def word_counter2(x,y):
    return len(x.split(y))

#part 2-3
def word_length(x):
    return [len(i) for i in x.split()]

#part 2-4
def primes(n):
    potential_prime = range(1,n+1)
    not_prime = []
    for num in potential_prime:
        idx = 2
        prime = True
        while idx <= num ** 0.5:
            if num % idx == 0:
                not_prime.append(num)
                break
            idx += 1
    return set(potential_prime) - set(not_prime)

#part 2-5
def divisors(lst,num):
    return ['yes' if i % num == 0 else 'no' for i in lst]

#part 2-6
def final_letter(phrase,letter):
    return [i for i in phrase if i[len(i)-1] == letter]

#part 2-7
def substring(lst_of_strings,substr):
    lst_of_strings = [x.lower() for x in lst_of_strings]
    substr = substr.lower()
    return [lst_of_strings.index(i) for i in lst_of_strings for a in range(len(i)-1) if i[a:(a+len(substr))]==substr]

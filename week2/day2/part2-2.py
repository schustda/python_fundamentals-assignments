x = str(raw_input("Enter the name of a State: ")).lower()
state_dictionary = {'Colorado': 'Denver', 'Alaska': 'Juneau', 'California': 'Sacramento',
                    'Georgia': 'Atlanta', 'Kansas': 'Topeka', 'Nebraska': 'Lincoln',
                    'Oregon': 'Salem', 'Texas': 'Austin', 'New York': 'Albany'}
z = "Unknown"
for i in state_dictionary:
    if i.lower() == x:
        z = state_dictionary[i]
print 'The capital of %s is %s' % (x.capitalize(),z)

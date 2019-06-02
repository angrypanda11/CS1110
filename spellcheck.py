

import urllib.request
stream = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/words.txt')
data_1 = stream.read().decode('utf-8').strip().split()
print('Type text; enter a blank line to end.')
refined = " "

while refined:
    sentence = input()
    refined = sentence.split()
    misspells = []
    for word in refined:
        words = word.strip('.?!,()"\'')
        if words not in data_1 and words.lower() not in data_1:
            misspells.append(words)
    for w in misspells:
        print(' MISSPELLED: ' + w)
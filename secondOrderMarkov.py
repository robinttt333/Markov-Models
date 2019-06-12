import urllib3
import random
from collections import defaultdict 
import nltk
http = urllib3.PoolManager()
text = http.request('GET','https://norvig.com/big.txt')       
text = text.data.decode('utf-8')
text = nltk.sent_tokenize(text)
d = defaultdict(list)
startingWords = []

for line in text:
    new_line = ""
    for word in line:
        if word != '"':
            new_line = new_line + word
    line = new_line
    if(len(line.split()) > 1):
        startingWords.append((line.split()[0],line.split()[1]))
    for w1,w2,w3 in zip(line.split(),line.split()[1:],line.split()[2:]):
        d[(w1,w2)].append(w3)

op = ""
a,b = random.choice(startingWords)
op = a + " " + b
while len(d[(op.split()[-2],op.split()[-1])]) > 0:
        new_word = random.choice(d[(op.split()[-2],op.split()[-1])])
        op = op + " " + new_word

while not op[0].isalpha(): 
    op = op[1:]
while op[-1]!= '.' and op[-1]!= '?' and op[-1]!= '!':
    op = op[:-1]
print(op)




import random;
import hashlib
import numpy as np
import matplotlib.pyplot as plt

def runBindSim(text,vote):
    simArray = [];
    simArray += [(0, 0)];
    numSim = 50;

    for x in range(1,17):
        totalcount = 0;
        average = 0;
        hexhash = hashlib.md5(text.encode()).hexdigest();
        hash = bin(int(hexhash, 16))[2:].zfill(128);
        hash = hash[:x];

        for i in range(1, numSim):
            tempCount = findBinding(hash, x, vote);
            totalcount = totalcount + tempCount;

        print("average for x = " + str(x) + ": ");
        average = totalcount / numSim;
        print(average);

        print("probability of breaking the binding property = " + str(numSim / totalcount));
        simArray += [(x, numSim / totalcount)];

    return simArray;

def runConcSim(text,vote):
    simArray =  [];
    simArray += [(0,0)];
    numSim = 100;

    for x in range (0,32):
        totalcount = 0;
        average = 0;
        hexhash = hashlib.md5(text.encode()).hexdigest();
        hash = bin(int(hexhash, 16))[2:].zfill(128);
        hash = hash[:x];

        for i in range(1, numSim):
            tempCount = findVote(hash, x, vote);
            totalcount = totalcount + tempCount;

        print("average for x = " + str(x) + ": ");
        average = totalcount / numSim;
        print(average);

        print("probability of breaking the concealing property = " + str(numSim/totalcount));
        simArray += [(x,numSim/totalcount)];

    return simArray;


def findVote(hash,x,vote):
    k = str(random.getrandbits(16));
    v = str(vote);
    guess = None;
    counter = 0;

    while (hash != guess):
        text = v + k;
        hexhash = hashlib.md5(text.encode()).hexdigest();
        guess = bin(int(hexhash, 16))[2:].zfill(128);
        guess = guess[:x];
        counter = counter + 1;

        k = str(random.getrandbits(16));

    return counter;

def findBinding(hash,x,vote):
    k = str(random.getrandbits(16));

    if(vote == 1):
        v = str(0);
    else:
        v = str(1);

    guess = None;
    counter = 0;

    while(hash != guess):
        text = v + k;
        hexhash = hashlib.md5(text.encode()).hexdigest();
        guess = bin(int(hexhash, 16))[2:].zfill(128);
        guess = guess[:x];

        counter = counter + 1;

        k = str(random.getrandbits(16));

    return counter;

k = str(random.getrandbits(16));
vote = 1;
text = str(vote) + k;

bindSim = runBindSim(text,vote);
print(bindSim);

#conSim = runConcSim(text, vote);
#print(conSim);

#plt.plot(conSim,'ro');
plt.plot(bindSim,'bo');

plt.axis([0, 33, 0, 0.01]);
plt.show();

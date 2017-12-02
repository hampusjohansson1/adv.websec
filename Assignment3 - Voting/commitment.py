import random;
import hashlib
import binascii;

def runBindSim(text):
    for x in range(1,17):
        totalcount = 0;
        average = 0;
        hexhash = hashlib.md5(text.encode()).hexdigest();
        hash = bin(int(hexhash, 16))[2:].zfill(128);
        hash = hash[:x];

        for i in range (1,100):
            tempCount = findBinding(hash,x);
            totalcount = totalcount + tempCount;
            average = totalcount // i;

        print("average for x = " + str(x) + ": ");
        print(average)
        print("probability of breaking the binding property = " + str(x / average));

def findBinding(hash,x):
    k = str(random.getrandbits(16));
    v = "0";

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
v = "1";

text = v + k;
runBindSim(text);



#hexhash = hashlib.md5(text.encode()).hexdigest();
#hash = bin(int(hexhash, 16))[2:].zfill(128);
#print(hash);
#a  = findBinding(hash,x);
#print(a);
import random;
import hashlib


def runBindSim(text):
    for x in range(1,4):
        totalcount = 0;
        average = 0;
        hash = hashlib.md5(text.encode("UTF-8")).hexdigest()[:x];
        for i in range (1,12):
            tempCount = findBinding(hash,x);
            totalcount = totalcount + tempCount;
            average = totalcount / i;
            print(average);

        print("average for " + str(x) + ": ");
        print(average);



def findBinding(hash,x):
    k = str(random.getrandbits(16));
    v = "0";

    guess = None;
    counter = 0;

    while(hash != guess):
        text = v + k;
        guess = hashlib.md5(text.encode("UTF-8")).hexdigest()[:x];

        counter = counter + 1;

        k = str(random.getrandbits(16));

    return counter;


k = str(random.getrandbits(16));
v = "1";

text = v + k;
#hash = hashlib.md5(text.encode("UTF-8")).hexdigest()[:4];
runBindSim(text);

#a  = findBinding(hash,4);
#print(a);
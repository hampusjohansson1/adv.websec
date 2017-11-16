from random import randint
import math;

def getCoin(u,k,c):
    iterations = 0;
    coins=0;
    bins = {};
    numberBins = int(math.pow(2, u));
    ball = 1;
    
    while coins < c:
        index = randint(0, numberBins);
        val = bins.get(index)
        
        if 	val != None:
              val = val + ball;
              if val == k:
                  coins = coins + 1;
                  del bins[index];
              else:
                  bins[index] = val;
        else:
            bins[index] = ball;
        
        iterations = iterations + 1;
        
    return iterations;

u=16;
k=2;
c=1;
confidence = 22 // 2;
sumIterations = 0;
simulations = 0;
meanVal = 0;
values = [];

iterations = getCoin(u,k,c);

newconf = confidence +1;

while newconf > confidence:
    print("newconf: ");
    print(newconf);
    
    deviation = 0;
    iterations = getCoin(u,k,c);
    
    sumIterations = iterations + sumIterations;
    simulations = simulations + 1;
    
    meanVal = sumIterations / simulations;
    
    values.append(meanVal);
    
    for val in values:
        deviation += ((meanVal - val) ** 2);
    
    deviation = math.sqrt(deviation // simulations);    
    newconf = meanVal + 3.66*(deviation // math.sqrt(sumIterations));
    
print(meanVal);
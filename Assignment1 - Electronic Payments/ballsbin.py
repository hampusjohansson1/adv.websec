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

u=20;
k=2;
c=10000;
confidence = 182 / 2;
sumIterations = 0;
simulations = 0;
meanVal = 0;
values = [];
firsttime = True;
iterations = 0
newconf = confidence +1;

while newconf > confidence:
     if firsttime is True:
         for x in range(0, 10):
             iterations = getCoin(u,k,c);
             simulations = simulations + 1;
             sumIterations = iterations + sumIterations;
             meanVal = sumIterations / simulations;
             values.append(meanVal);
           
     deviation = 0;
     iterations = getCoin(u,k,c);
    
     sumIterations = iterations + sumIterations;
     simulations = simulations + 1;
    
     meanVal = sumIterations / simulations;
     values.append(meanVal);
    
     for val in values:
         deviation += ((val - meanVal) ** 2);
    
     standarddeviation = math.sqrt((deviation / simulations));
    
     newconf = 3.66*(standarddeviation / math.sqrt(simulations));
     firsttime = False;
    
print(meanVal);
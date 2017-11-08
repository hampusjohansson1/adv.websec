from random import randint
import math;

u=16;
k=2;
c=1;

numberBins = int(math.pow(2, u));

sumIterations = 0;
simulations = 10000;
bins = {};

for x in range(0, simulations):
    iterations = 0;
    coins=0;
    bins.clear()
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
        
    sumIterations = iterations + sumIterations;
    
print(sumIterations);   
meanVal = sumIterations // simulations;

print("mean value");
print (meanVal);



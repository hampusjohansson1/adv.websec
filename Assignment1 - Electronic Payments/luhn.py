import re;
import math;

def luhn(numbers):
    sum = 0;
    digits = len(numbers);
    par = digits % 2;
    even = False;

    for i, val in enumerate(numbers):
        if val == "X":
            if i % 2 == par:
                even = True;
        else:
            val = int(val);
            if i % 2 == par:
                val = val * 2;
                if val > 9:
                    val = val -9;              
            sum = sum + val;
        
    tenth = int(math.ceil(sum / 10.0)) * 10
    luhn = tenth - sum;
    
    if(even == True):
        if(luhn % 2 == 0):
            luhn = luhn // 2;
        else:
          luhn = (luhn + 9) // 2;
        
    return luhn;

file = open("luhn.txt", "r")
numberarray = [line.rstrip('\n') for line in file]
product = list(map(luhn,numberarray));
print ("".join(str(x) for x in product));






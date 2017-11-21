import re;
import math;
import operator;

def format(s, x):
        s = "{0:0{1}X}".format(s,x);
        return s;

def getAnswer(SA,SB,DA,DB,M,b):
    if(b == 0):
        myBroad = SA ^ SB;
        message = (DA ^ DB) ^ myBroad;
        
        message = format(message,4);
        myBroad = format(myBroad,4);
        
        if(message == 0):
            message += 000;
        
        return myBroad + message;

    elif(b==1):
        sentMess = (SA ^ SB) ^ M;
        return format(sentMess,4);

    return "Nothing to return";

SA = 0x0C73;
SB = 0x80C1;
DA = 0xA2A9;
DB = 0x92F5;
M = 0x9B57;
b = 1;

#SA = 0x27C2;
#SB = 0x0879;
#DA = 0x35F6;
#DB = 0x1A4D;
#M = 0x27BC;

answer = getAnswer(SA,SB,DA,DB,M,b);   

print(answer);






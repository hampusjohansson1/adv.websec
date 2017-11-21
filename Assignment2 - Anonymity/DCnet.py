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

SA = 0xBF0D;
SB = 0x3C99;
DA = 0x186F;
DB = 0x2EAD;
M = 0x62AB;
b = 0;

#SA = 0x27C2;
#SB = 0x0879;
#DA = 0x35F6;
#DB = 0x1A4D;
#M = 0x27BC;

answer = getAnswer(SA,SB,DA,DB,M,b);   

print(answer);






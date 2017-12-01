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

SA = 0x0E53;
SB = 0xA248;
DA = 0x1C67;
DB = 0xB07C;
M = 0x7618;
b = 0;

#SA = 0x27C2;
#SB = 0x0879;
#DA = 0x35F6;
#DB = 0x1A4D;
#M = 0x27BC;

answer = getAnswer(SA,SB,DA,DB,M,b);   
print("Answer:")
print(answer);






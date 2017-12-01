import re;
import math;
import operator;

def exclusion(learnList,badguysets):
    for badset in badguysets:
        before = False;
        templearn = learnList.copy();
        
        for i,learnSet in enumerate(learnList):
            if len(badset.intersection(learnSet)) > 0 and before == False:
                templearn[i] = badset.intersection(learnSet);
                before = True;
            elif len(badset.intersection(learnSet)) > 0:
                before = False;
                break;
        
        if before == True:
            learnList = templearn.copy();
            
    return learnList;

def extractSets(mixIP,badIP,file):
    tempSet = set();
    returnList = [];
    badSent = False;
    nextPack = 0;
    
    for i,pkt in enumerate(file.packets):
        ip_src = pkt.packet.payload.src.decode('UTF8')
        ip_dst = pkt.packet.payload.dst.decode('UTF8')
        
        if(i == (len(file.packets)-1)):
            nextPack = None;
        else:
            nextPack = file.packets[i+1].packet.payload.src.decode('UTF8');
        
        if(ip_src == badIP):
            badSent = True;
            
        if badSent == True and ip_src == mixIP:
            tempSet.add(ip_dst);
            if (nextPack != mixIP or nextPack == None):
                returnList.append(tempSet.copy());
                tempSet.clear();
                badSent = False;
                    
    return returnList;

def learn(badlist,partners):
    learnList = [];
    
    for badset in badlist:
        intersect = False;
        if(len(learnList) == 0):
                learnList.append(badset.copy());
        else:
            for myset in learnList:
                if len(myset.intersection(badset)) > 0:
                     intersect = True;
                     break;
                        
            if(intersect == False):
                learnList.append(badset);
                   
            if(len(learnList) >= partners):
                return learnList;

    return learnList;
    
def extractSum(partnerlist):
    sum = 0;
    for myset in partnerlist:
         a = myset.pop().split('.');
         iphex = '{:02X}{:02X}{:02X}{:02X}'.format(*map(int, a));
         sum = sum + int(iphex,16);
    return sum;
    
from pcapfile import savefile
#testcap = open('test.pcap', 'rb')
testcap = open('cialog.pcap', 'rb')
capfile = savefile.load_savefile(testcap, layers=2, verbose=True)

#mixIP = "94.147.150.188";
#badIP = "159.237.13.37";
badIP = "245.221.13.37";
mixIP = "15.24.22.93";
partners = 9;

badguysets = extractSets(mixIP,badIP,capfile);
print(len(badguysets));

learnList = learn(badguysets,partners);
print(len(learnList));

print("Partners:");
partnerlist = exclusion(learnList,badguysets);
print(partnerlist);

print("Sum:");
sum = extractSum(partnerlist);
print(sum);
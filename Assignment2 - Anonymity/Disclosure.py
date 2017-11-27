import re;
import math;
import operator;

def exclusion(learnList,badguysets):
    for badset in badguysets:
        before = False;
        templearn = learnList;
        
        for i,set in enumerate(learnList):
            if len(badset.intersection(set)) > 0 and before == False:
                templearn[i] = badset.intersection(set);
                before = True;
            elif len(badset.intersection(set)) > 0:
                before = False;
                break;
        
        if before == True:
            learnList = templearn;
            
    return learnList;

def learn(partners,list):
    learnList = [];
    
    while len(learnList) < 12:
        candidate = list.pop();
        intersect = False;
        
        if len(learnList) == 0:
               candcopy = candidate.copy();
               learnList.append(candcopy);
        
        for set in learnList:
            if len(set.intersection(candidate)) > 0:
                intersect = True;
                break;
        
        if(intersect == False):
            candcopy = candidate.copy();
            learnList.append(candcopy);
            #candidate.clear();
               
    return learnList;

def extractSets(mixIP,badIP,file):
    badSent = False;
    prevSrc = 0;
    tempSet = set();
    setList = [];
    
    for i,pkt in enumerate(file.packets):
        timestamp = pkt.timestamp
        eth_src = pkt.packet.src.decode('UTF8')
        eth_dst = pkt.packet.dst.decode('UTF8')
        ip_src = pkt.packet.payload.src.decode('UTF8')
        ip_dst = pkt.packet.payload.dst.decode('UTF8')
        
        if((prevSrc == mixIP and ip_src != mixIP) or i == len(file.packets)-1) and badSent == True:                
            prevSrc = ip_src;
            badSent = False;
            tempcopy = tempSet.copy();
            setList.append(tempcopy);
            tempSet.clear();
            
        if(ip_src == badIP):
            badSent = True;
        
        if(badSent and ip_src == mixIP):
            tempSet.add(ip_dst);
            prevSrc = ip_src;
            
    return setList;
    
def extractSum(partnerlist):
    sum = 0;
    for set in partnerlist:
         a = set.pop().split('.');
         iphex = '{:02X}{:02X}{:02X}{:02X}'.format(*map(int, a));
         sum = sum + int(iphex,16);
    return sum;
    
from pcapfile import savefile
#testcap = open('test.pcap', 'rb')
testcap = open('cialog.pcap', 'rb')
capfile = savefile.load_savefile(testcap, layers=2, verbose=True)

#mixIP = "94.147.150.188";
#badIP = "159.237.13.37";
badIP = "161.53.13.37";
mixIP = "11.192.206.171";
partners = 12;

badguysets = extractSets(mixIP,badIP,capfile);

learnList = learn(partners,badguysets);
print(learnList);

print("Partners");
partnerlist = exclusion(learnList,badguysets);
print(partnerlist);

print("Sum:");
sum = extractSum(partnerlist);
print(sum);
import re;
import math;
import operator;

def exclusion(learnList,badguysets):
    for badset in badguysets:
        before = False;
        templearn = learnList;
        
        for i,myset in enumerate(learnList):
            if len(badset.intersection(myset)) > 0 and before == False:
                templearn[i] = badset.intersection(myset);
                before = True;
            elif len(badset.intersection(myset)) > 0:
                before = False;
                break;
        
        if before == True:
            learnList = templearn;
            
    return learnList;

def learn(partners,list):
    learnList = [];
    tempCand = list.pop();
    learnList.append(tempCand);
    intersect = False;
    
    while len(learnList) < partners:
        candidate = list.pop();
        intersect = False;

        for myset in learnList:
            if len(myset.intersection(candidate)) > 0:
                intersect = True;
            
        if(intersect == False):
            learnList.append(candidate.copy());
            candidate.clear();
        
        if(len(learnList) >= partners):
                return learnList;
        
    return learnList;

def extractSets(mixIP,badIP,file):
    badSent = False;
    nextPack = 0;
    tempSet = set();
    setList = [];
    
    for i,pkt in enumerate(file.packets):
        ip_src = pkt.packet.payload.src.decode('UTF8')
        ip_dst = pkt.packet.payload.dst.decode('UTF8')
        
        if(ip_src == badIP):
            badSent = True;
            
        if(i == (len(file.packets)-1)):
            nextPack = None;
        else:
            nextPack = file.packets[i+1].packet.payload.src.decode('UTF8');
            
        if(badSent and ip_src == mixIP):
            tempSet.add(ip_dst);
            
            if (nextPack != mixIP or nextPack == None):              
                badSent = False;
                tempcopy = tempSet.copy();
                setList.append(tempcopy);
                tempSet.clear();
            
    return setList;
    
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
badIP = "161.53.13.37";
mixIP = "11.192.206.171";
partners = 12;

badguysets = extractSets(mixIP,badIP,capfile);
print(len(badguysets));

learnList = learn(partners,badguysets);
#print(learnList);

print("Partners");
partnerlist = exclusion(learnList,badguysets);
print(partnerlist);

print("Sum:");
sum = extractSum(partnerlist);
print(sum);
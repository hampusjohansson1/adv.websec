import re;
import math;
import operator;


def findBadguy(mixIP,badIP,file,partners):
    returnSet = set();
    tempSet = set();
    badSent = False;
    collectData = False;
    prevSrc = 0;
    
    for pkt in capfile.packets:
        timestamp = pkt.timestamp
        # all data is ASCII encoded (byte arrays). If we want to compare with strings
        # we need to decode the byte arrays into UTF8 coded strings
        eth_src = pkt.packet.src.decode('UTF8')
        eth_dst = pkt.packet.dst.decode('UTF8')
        ip_src = pkt.packet.payload.src.decode('UTF8')
        ip_dst = pkt.packet.payload.dst.decode('UTF8')
        
        if(prevSrc == mixIP and ip_src != mixIP):
            prevSrc = ip_src;
            
            if(len(returnSet) == 0):
                returnSet = tempSet;
            
            elif(len(tempSet) > 0):
                 returnSet = returnSet.intersection(tempSet);
           
            tempSet.clear();
            badSent = False;
        
        if(ip_src == badIP):
            badSent = True;
        
        if(badSent and ip_src == mixIP):
            tempSet.add(ip_dst);
            prevSrc = ip_src;
        
    return returnSet;
        
        #print ('{}\t\t{}\t{}\t{}\t{}'.format(timestamp, eth_src, eth_dst, ip_src, ip_dst))
    
from pcapfile import savefile
testcap = open('test.pcap', 'rb')

# print the packets
print ('timestamp\teth src\t\t\teth dst\t\t\tIP src\t\tIP dst')

capfile = savefile.load_savefile(testcap, layers=2, verbose=True)

mixIP = "94.147.150.188";
badIP = "159.237.13.37";
partners = 2;

badguys = findBadguy(mixIP,badIP,capfile,partners);

print(badguys);


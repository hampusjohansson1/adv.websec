import hashlib
import math;
import binascii
import os,codecs;


def I2OSP(x, xLen):
    output = [];
    stringOut = "";
    length = xLen-1;

    a = bytearray();

    for i in range (0,xLen):
        output.append(x % 256);
        x = x // 256;
        length = (length -1);

    for nbr in reversed(output):
        a.insert(len(a),nbr);

    return a;


def MGF1 (mgfSeed, maskLen):
    T = "";
    m = hashlib.sha1(mgfSeed.encode("utf-8"));
    hLen = len(m.digest());

    mgfSeed = bytearray.fromhex(mgfSeed);

    for x in range(0, math.ceil(maskLen / hLen)):
        C = I2OSP(x,4);
        T = T + hashlib.sha1((mgfSeed + C)).hexdigest();

    return T[:maskLen*2];

def OAEPencode(message):
    L = "";
    k = 128;
    mLen = len(bytearray.fromhex(message));
    hLen = 20;
    lHash = hashlib.sha1(L.encode("utf-8")).digest();
    PS = bytearray();

    for x in range(0,(k - mLen - 2*hLen - 2)):
        PS.append(0);

    DB = lHash + PS +  bytearray.fromhex("01") + bytearray.fromhex(message);

    seed = "1e652ec152d0bfcd65190ffc604c0933d0423381";
    dbMask = MGF1(seed,k-hLen-1);

    maskedDB = hex(int(DB.hex(), 16) ^ int(dbMask, 16));
    maskedDB = str(maskedDB)[2:];

    seedMask = MGF1(maskedDB,hLen);
    maskedSeed = hex(int(seed, 16) ^ int(seedMask, 16));
    maskedSeed = str(maskedSeed)[2:];

    print("maskedSeed: " + maskedSeed);
    print("MaskedDB: " + maskedDB);

    EM = "0000" + maskedSeed + maskedDB;

   # print(EM);

    return EM;

def OAEPdecode(EM):
    L = "";
    k = 128;
    hLen = 20;
    lHash = hashlib.sha1(L.encode("utf-8")).digest();

    EM = EM[4:];
    maskedSeed = EM[:hLen*2-2];
    maskedDB = EM[hLen*2-2:];

    return EM;

#mgfSeed = "0123456789abcdef";
#maskLen = 30;
#output = MGF1(mgfSeed,30);
#print(output);

message = "fd5507e917ecbe833878";
EM = OAEPencode(message);
OAEPdecode(EM);
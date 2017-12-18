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


def MGF1(mgfSeed, maskLen):
    T = "";
    m = hashlib.sha1(mgfSeed.encode("utf-8"));
    hLen = len(m.digest());

    mgfSeed = bytearray.fromhex(mgfSeed);

    for x in range(0, math.ceil(maskLen / hLen)):
        C = I2OSP(x,4);
        T = T + hashlib.sha1((mgfSeed + C)).hexdigest();

    return T[:maskLen*2];

def OAEPencode(message,seed):
    L = "";
    k = 128;
    mLen = len(bytearray.fromhex(message));
    hLen = 20;
    lHash = hashlib.sha1(L.encode("utf-8")).digest();
    PS = bytearray();

    for x in range(0,(k - mLen - (2*hLen) - 2)):
        PS.append(0);

    DB = lHash + PS +  bytearray.fromhex("01") + bytearray.fromhex(message);

    dbMask = MGF1(seed,k-hLen-1);

    maskedDB = hex(int(DB.hex(), 16) ^ int(dbMask, 16));
    maskedDB = str(maskedDB[2:]);

    seedMask = MGF1(maskedDB,hLen);
    maskedSeed = hex(int(seed, 16) ^ int(seedMask, 16));
    maskedSeed = str(maskedSeed[2:]);

    EM = "00" + maskedSeed + maskedDB;

    return EM;

def OAEPdecode(EM):
    L = "";
    k = 128;
    hLen = 20;
    M = "";

    EM = EM[2:];
    maskedSeed = EM[:hLen*2];
    maskedDB = EM[hLen*2:];

    seedMask = MGF1(maskedDB, hLen);

    seed = hex(int(maskedSeed, 16) ^ int(seedMask, 16))[2:];

    dbMask = MGF1(seed, k - hLen - 1);

    DB = hex(int(maskedDB, 16) ^ int(dbMask, 16))[2:];

    #remove lHash
    DB = DB[hLen*2:];

    for i,c in enumerate(DB):
        if c == "1":
            M = DB[i+1:];
            break;

    return M;


mgfSeed = "ea099bc94775bbe620ffde094e8ee1aa049d4894";
maskLen = 22;
mgf = MGF1(mgfSeed,maskLen);
print("MGF1 seed: " + mgf);

message = "0b12625e83ce789cbcc60e9f469b76f95fcd76815eb508470892be8a56";
seed = "1e652ec152d0bfcd65190ffc604c0933d0423381";

EM = OAEPencode(message,seed);
print("message encode: " + EM);

mesret = OAEPdecode("00b2f73d91326091417ed768c1bab03bdf7d32cb15d2345866989457444e4884695e81d6241ec8130c631733247498de28d4b5acfa50496127730f60b29cfad2157ca073fc373e40305f7eaeadcd30a7d591185f84876ca9e9d417f8441127dfb137ff4faf8437bd955e5dc03ed9094e6ea8429fa67e15173c42b2839afbd156");
print("messege decode: " + mesret);
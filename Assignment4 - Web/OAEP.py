import hashlib
import math;
import binascii


def I2OSP(x, xLen):
    output = [];
    stringOut = "";
    length = xLen-1;

    a = bytearray();

    for i in range (0,xLen):
        output.append(x % 256);
        x = x // 256;
        length = (length -1);
    print(output);

    for nbr in reversed(output):
        a.insert(len(a),nbr);

    print(a);
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

def OAEPencode(Message,seed):

    return Message;

mgfSeed = "0123456789abcdef";
maskLen = 30;

output = MGF1(mgfSeed, maskLen);

print(output);
print(len(output));
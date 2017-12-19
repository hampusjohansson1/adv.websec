import base64;

def padding(hex_val):
    if int(hex_val, 16) > 7:
        return True;
    else:
        return False;

def shortDef(hexStr):
    length = int(len(hexStr) // 2);

    if (length < 2):
        length = 1

    newlen = hex(length).replace("0x","")

    if (len(newlen) % 2 != 0):
        return "0" + newlen

    return newlen

def longDef(hexStr):
    length = hex(int(len(hexStr) // 2));
    newlen = length.replace("0x","");

    if (len(newlen) % 2 != 0):
        newlen = "0" + newlen

    if(len(hexStr) >= 508):
        return "82" + newlen

    else:
        return "81" + newlen

def encode(integer,t = "02"):
    v = hex(integer)[2:];

    if (len(v) % 2 != 0):
        v = "0" + v

    if padding(v[0:1]):
        v = "00" + v;

    if len(v) <= 254:
        l =shortDef(v);
    else:
        l = longDef(v);

    return t + l + v;

def egcd(a, b):
	x,y, u,v = 0,1, 1,0
	while a != 0:
		q, r = b//a, b%a
		m, n = x-u*q, y-v*q
		b,a, x,y, u,v = a,r, u,v, m,n
	return b, x, y

def modinv(a, m):
	g, x, y = egcd(a, m)
	if g != 1:
		return None
	else:
		return x % m


def createRSA(p,q,e):
    phi = (p-1)*(q-1);

    n = p * q;
    d = modinv(e,phi);
    coefficient = modinv(q,p);

    exponent1 = d % (p - 1);
    exponent2 = d % (q - 1);

    version = 0;

    rsa = encode(version) + encode(n) + encode(e) + encode(d) \
          + encode(p) + encode(q) + encode(exponent1) + encode(exponent2) + encode(coefficient);


    RSAder = encode(int(rsa,16),"30");
    print("DER encoded key:")
    print(RSAder);
    base64rsa = base64.b64encode(bytes.fromhex(RSAder));

    return base64rsa.decode("utf-8");

p = 125544725288804755629407902767424226511244274133170826741356714374102442017028867604161662842961872367812002506492977865510281655586893284680569220846024095212331084185987610111846793778566373654726905108122665926894428124379355505383446846960279303274818462581753651130265314120067773473047298112241224515929;
q = 156896790717869302247135125903842092110191364805167470756303077405193189346279911346626091902070263081446488324619819545008434675946609302184457727180818687245280721811046734152638059542402509267193424902609221513050411772163945055475159060884174089543329324197322420117740007778643458132726492259521836559287;
e = 65537;

key = createRSA(p,q,e);
print("Base64 encoded key:")
print(key);

nbr = 163435854098740093663299652322731784552890627454094830790739571168259800890255172471317604520083242192906756366634235845075288028116039200341019084422428500406794845549632205439050129329536883818179626098659035579423302545972504356467173349834092717067647980583474301300249983953880165923728031427632624831641
print ("DER encoded integer:")
print(encode(nbr))


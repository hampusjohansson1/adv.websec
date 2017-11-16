import hashlib

def merkleTree(hexarray,start):
        if not hexarray:
              return start;
        else:
            if hexarray[0][0] == 'L':
                start = bytearray.fromhex(hexarray.pop(0)[1:] + start)
                
            elif hexarray[0][0] == 'R':
                start = bytearray.fromhex(start + hexarray.pop(0)[1:])
                        
        start = hashlib.sha1(start).hexdigest()            
        return merkleTree(hexarray,start);
                    
file = open("merkleSPV.txt", "r")
hexarray = [line.rstrip('\n') for line in file]

merkleTreeRoot = merkleTree(hexarray,hexarray.pop(0));
print(merkleTreeRoot);

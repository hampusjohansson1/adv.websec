import hashlib

def createHash(leftstr,rightstr):
    bytes = bytearray.fromhex(leftstr + rightstr)
    Hash = hashlib.sha1(bytes).hexdigest()
    return Hash

def createTree(tree):
    left = None;
    right = None;
    level = [];
    
    for i, leaf in enumerate(tree):
        if not tree:
                  return createTree(level);
        
        if i % 2 == 0
            left = Node(leaf)
        else:
            right = Node(leaf)       
    
        if left != None and right != None:
            Hash = createHash(left,right)
            level.append(Node(Hash, left, right))
            left = None;
            right = None;
       
file = open("merkleTree.txt", "r")
hexarray = [line.rstrip('\n') for line in file]

merkleTree = creteTree(hexarray)

class Node:
    def __init__(self, left=None, right=None):
        self.left  = left
        self.right = right

    def __str__(self):
        return str(self)
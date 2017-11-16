import hashlib

def createPair(leftNode,RightNode):
    newNode = bytearray.fromhex(leftNode + RightNode);
    newNodeHash = hashlib.sha1(newNode).hexdigest();
    return newNodeHash;

def createTree(currentList,returnArray,index):
     newList = [];
     leftNode = None;
     rightNode = None;
     
     if len(currentList) is 1:
         returnArray.append(currentList.pop());
         return returnArray
        
     if (len(currentList) % 2) != 0:
         currentList.append(currentList[-1]);
     
     for i, leaf in enumerate(currentList):
        if i % 2 is 0:
             leftNode=leaf;
             if i is index:
                 index = index // 2;
                 returnArray.append("R" + currentList[i+1]);
                 
        elif i % 2 != 0:
             rightNode = leaf;
             if i is index:
                 index = (index - 1) // 2;
                 returnArray.append("L" + currentList[i-1]);
        
        if leftNode != None and rightNode != None:
            nextNode = createPair(leftNode,rightNode);
            newList.append(nextNode);
            leftNode = None;
            rightNode = None;
     
     currentList = newList;
     return createTree(currentList,returnArray,index);
         
file = open("merkleTree.txt", "r")
hexArray = [line.rstrip('\n') for line in file]
returnArray = [];

index = int(hexArray[0]);
del hexArray[0];

depth = int(hexArray[0]);
del hexArray[0];

merkleTree = createTree(hexArray,returnArray,index);

for line in merkleTree:
    print (line);

print(merkleTree[len(merkleTree) - depth-1] + merkleTree[-1]);
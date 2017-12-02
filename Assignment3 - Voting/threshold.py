import numpy as np

myPoly = [9,19,5];

myX = 1;
myY = 0;

for i,val in enumerate(myPoly):
    temp = val*(myX**i);
    myY = myY + temp;

f1 = [myY,37,18,40,44,28];
totf1 = np.sum(f1);

points = np.array([(1, totf1),(4, 1385),(5, 2028)])
x = points[:,0]
y = points[:,1]

z = np.polyfit(x, y, len(points)-1)
f = np.poly1d(z)

print(f[0]);

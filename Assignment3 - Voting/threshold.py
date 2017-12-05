import numpy as np

myPoly = [2,12,20,18];

myX = 1;
myY = 0;

for i,val in enumerate(myPoly):
    temp = val*(myX**i);
    myY = myY + temp;

f1 = [myY,44,23,34,41,42];
totf1 = np.sum(f1);

points = np.array([(1, totf1),(3, 2930),(5, 11816),(6, 19751)])
x = points[:,0]
y = points[:,1]

z = np.polyfit(x, y, len(points)-1)
f = np.poly1d(z)

print(f[0]);

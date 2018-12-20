import numpy as np
a=np.array([[1,-2,0,-1],[0,1.5,-0.5,-1],[-1,1,0.5,-1],])
w=np.array([1,-1,0,0.5])  
d=[-1,-1,1]
c=0.1
for iter in range(1,7):
    print "iteration" ,(iter)
    for i,x in enumerate(a):
        net=np.dot(a[i],w)
        if net>=0:
           out=1
        else:
           out=-1
        r=d[i]-out
        delta=c*r*a[i]
        w=w+delta
        print i,w


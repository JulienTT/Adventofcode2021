import sys
#import numpy as np
import copy
#from functools import lru_cache,wraps
from operator import itemgetter,countOf
#import matplotlib.pyplot as plt

from collections import Counter

def read_file(file_name):
    with open(file_name) as input_file:
        list_of_lines=input_file.read().splitlines()
    i=0;
    operations=[]
    for line in list_of_lines:
        List=line.split(' ')
        
        if 'on' in List[0]:
            op=True
        else:
            op=False
        List[1]=List[1].replace('x=','')
        List[1]=List[1].replace('y=','')
        List[1]=List[1].replace('z=','')
        List[1]=List[1].split(',')
        X=List[1][0].split('..')
        Y=List[1][1].split('..')
        Z=List[1][2].split('..')
        operations.append((op,int(X[0]),int(X[1]),int(Y[0]),int(Y[1]),int(Z[0]),int(Z[1])))
    return operations

def Is_In(x,y,z,op):
    return x>=op[1] and x<=op[2] and y>=op[3] and y<=op[4] and z>=op[5] and z<=op[6]

def Rules(x,y,z,Operations):
    n=0
    for op in reversed(Operations):
        if x>=op[1] and x<=op[2] and y>=op[3] and y<=op[4] and z>=op[5] and z<=op[6]:
            return True if op[0]==1 else False
    return False
    
if __name__ == '__main__':
    Operations = read_file('input')
    X,Y,Z=[],[],[]
    for i in Operations:
        X.extend([i[1],i[2]+1])
        Y.extend([i[3],i[4]+1])
        Z.extend([i[5],i[6]+1])
    X = list(dict.fromkeys(X))
    Y = list(dict.fromkeys(Y))
    Z = list(dict.fromkeys(Z))

    X.sort()
    Y.sort()
    Z.sort()

    Nb = 0
    Operations.reverse()
    
    for x, xp in zip(X, X[1:]):
        print("x={}".format(x))
        Operations_x = [(a, x0, x1, y0, y1, z0 ,z1) for a, x0, x1, y0, y1, z0 ,z1 in Operations if x0 <= x <= x1]
        for y, yp in zip(Y, Y[1:]):
            Operations_y = [(a, x0, x1, y0, y1, z0, z1) for a, x0, x1, y0, y1, z0, z1 in Operations_x if y0 <= y <= y1]
            for z, zp in zip(Z, Z[1:]):
                Operations_z = [(a, x0, x1, y0, y1, z0, z1) for a, x0, x1, y0, y1, z0, z1 in Operations_y if z0 <= z <= z1]
                if Operations_z and Operations_z[0][0]:
                    Nb += (xp - x) * (yp - y) * (zp - z)

    print(Nb)

def next4num(n):
    a=(n*2+1)**2
    b=a-2*n
    c=b-2*n
    d=c-2*n
    return [a,b,c,d]
from math import sqrt
def prime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
numprime=3
total=5
counter=2
while numprime/total>=0.1:
    a,b,c,d=next4num(counter)
    if prime(a):
        numprime+=1
    if prime(b):
        numprime+=1
    if prime(c):
        numprime+=1
    if prime(d):
        numprime+=1
    total+=4
    counter+=1
print(((counter-1)*2)+1)

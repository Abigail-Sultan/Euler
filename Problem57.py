def next(t,b):
    nb=t+b
    nt=nb+b
    return nt,nb
def checkdidgits(t,b):
    if len(str(t))>len(str(b)):
        return True
    return False 
c=0
t=1
b=1
for i in range(1,1001):
    t,b=next(t,b)
    if checkdidgits(t,b)==True:
        c+=1

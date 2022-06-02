import random as r
import math
print("You have paid $100")
sn=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
n=[1,2,3,4,5,6,7,8,10,20,50,75,100,150,250,500]
yn=0
earned=0
d=0
for x in range(0,len(sn),1):
    print(sn[x])
a=int(input("Pick up your case out of the given cases    "))
sn.remove(a)

c=0
for xx in range(1,5,1):
    for xxx in range(0,(6-xx),1):
        print("")
        for x in range(0, len(sn), 1):
            print(str(sn[x])+"        "+str(n[x]))
        print("          "+str(n[len(n)-1]))
        a = int(input("Pick up any case out of the given cases     "))
        sn.remove(a)
        b = r.randint(0, len(n)-1)
        print("Your case was " +str(n[b]))
        n.pop(b)
    print("")
    c=str(input("Computer is giving you a deal of "+str((math.floor((sum(n))/(len(n)))))+"$. Do you accept it?    "))
    c=c.lower()
    if c=="yes":
        break
    else:
        continue

print("")
if c=="yes":
    print("You put in 100$ and got back "+str(math.floor((sum(n))/(len(n))))+"$ earning "+str(((math.floor((sum(n))/(len(n)))-100)))+"$")
else:
    b = r.randint(0, len(n)-1)
    yn = n[b]
    n.pop(b)
    print("Lets open your case")
    print("Your case had " + str(yn))
    print("You put in 100$ and got back " + str(n[0]) + "$ earning " + str(n[0] - 100) + "$")














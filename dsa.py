import random
import hashlib

def checkprime(num):
	i=2
	n=int(num)
	while (i<=n/2):
		if n%i==0:
			return False
		i+=1
	return True

def checktuple(p,q):
	if not checkprime(p):
		print "P is not Prime"
		return False
	if not checkprime(q):
		print "Q is not Prime"
		return False
	if (p-1)%q!=0:	
		print "P is not a prime modulus of Q"
		return False
	return True

def get_g(p,q,h):
	for g in range (1,p):
		if pow(g,q)%p!=1 or g!=pow(h,(p-1)/q)%p:
			g+=1
		else:
			return g
	return -1

while True:
	p=raw_input("Enter P")
	q=raw_input("Enter Q")
	p=int(p)
	q=int(q)
	if checktuple(p,q):
		break
	else:
		print "Invalid Values."
m=hashlib.sha1()
msg=raw_input("Enter Message")
m.update(msg)
h=int(str(m.hexdigest()),16)
g=get_g(p,q,h)

while True:
	x=raw_input("Enter x such that 1<x<Q")
	x=int(x)
	if x<1 or x>q:
		print "Enter correct value of x" 
	else:
		break
y=pow(g,x)%p
print "Public Key: " ,[p,q,g,y]
print "Private Key: " ,[p,q,g,x]
k=random.randint(1,q)
r=(pow(g,k)%p)%q
i=0
while True:
	if(k*i)%q==1:
		break
	i+=1
s=i*(h+r*x)

print "DSA Key Generated: ", [r,s]

print "Verifying..."

w=0
while True:
	if (w*s)%q==1:
		break
	w+=1
u1=(h*w)%q
u2=(r*w)%q
v=((pow(g,u1)*pow(y,u2))%p)%q

if(r==v):
	print "Keys Verified!"
else:
	print "Keys not verified."
				

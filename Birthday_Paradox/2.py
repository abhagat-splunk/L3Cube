import random
import matplotlib.pyplot as plt
def prac(n):
	s=0.0
	for j in range(1000):
		temp=list()
		for i in range(n):
			z=random.randint(0,365)
			temp.append(z)
		t=set(temp)
		if len(t)<n:
			s+=1
	s=s/10.0
	return s
def theory(n):
	num=1.0
	q=1.0
	for i in range(n):
		num=num*(365-i)
		q=q*365
	ans=num/q
	ans=1-ans
	ans=ans*100
	return ans
xp=list()
yp=list()
xt=list()
yt=list()
for i in range(367):
	xp.append(i)
	yp.append(prac(i))
	xt.append(i)
	yt.append(theory(i))
lp=plt.plot(xp,yp)
lt=plt.plot(xt,yt)
plt.setp(lp,color='r')
plt.setp(lt,color='b')
plt.show()

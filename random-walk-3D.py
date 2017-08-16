import random
import matplotlib.pyplot as plt
men=5000
steps=1000
posn={}
count={}
x=[]
y=[]
for i in range(men):
	add=0
	for j in range(steps):
		if(random.random()>0.5):
			add=1
		else:
			add=-1
		if(posn.get(i)):
			posn[i]+=add
		else:
			posn[i]=add

# for i in range(men):
# 	if(posn.get(i)):
# 		print(str(i)+":"+str(posn[i]))
for i in range(men):
	if(posn.get(i)):
		if(posn[i]<0):
			posn[i]=-1*posn[i]
		if(count.get(posn[i])):
			count[posn[i]]+=1
		else:
			count[posn[i]]=1

# for i in range(steps):
# 	if(count.get(i)):
# 		print(str(i)+":"+str(count[i]))

plt.xlabel('Radius')
plt.ylabel('No of Men')
plt.title('Random Walk Sphere')
for i in range(steps):
	if(count.get(i)):
		x.append(i)
		y.append(count[i])
plt.plot(x,y)
plt.show()
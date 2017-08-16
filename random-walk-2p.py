import random
import matplotlib.pyplot as plt
trials=5000
steps=1000
count={}
x=[]
y=[]
for i in range(trials):
	man1=0
	man2=0
	for j in range(steps):
		if(random.random()>0.5):
			man1-=1
		else:
			man1+=1
		if(random.random()>0.5):
			man2-=1
		else:
			man2+=1
		if(man1==man2):
			if(count.get(j)):
				count[j]+=1.0
			else:
				count[j]=1.0
# for i in range(steps):
# 	if(count.get(i)):
# 		print(str(i)+":"+str(count[i]))

plt.xlabel('Step-No.')
plt.ylabel('Probablity')
plt.title('Random Walk 2 Persons')
for i in range(steps):
	if(count.get(i)):
		x.append(i)
		y.append(count[i]/trials)
plt.plot(x,y)
plt.show()
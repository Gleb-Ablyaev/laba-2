k=int(input("k="))
f=open('laba 2.txt','r')
data=f.read()
mass=data.split('.')
mass2=[]
i=1
for i in range(0,len(mass)):
    mass2.append(mass[i].split())
    if len(mass2[i])==k:
        print(mass[i],'.')
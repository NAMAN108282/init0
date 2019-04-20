from datetime import datetime,date,time
bool=0
pi=0
t1=datetime.now().timestamp()
for i in range(1,10000000000,2):
    if bool==1:
        pi=pi-1/i
        bool=0
    else:
        pi=pi+1/i
        bool=1
	
print(pi*4)
t2=datetime.now().timestamp()
print(t2-t1)

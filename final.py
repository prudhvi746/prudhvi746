from threading import *
from time import *
class Semaphor:
    def __init__(self,semaphor):
        self.semaphor=semaphor
    def requestResource(self,count,i):
        if(count<self.semaphor):
            print("process ",i," resource allocated")
            self.semaphor-=count
            sleep(10)
            print("\nprocess ",i," Process completed! Releasing the resources")
            self.semaphor+=count
            
        else:
            print("process ",i," Resource not allocated waiting")
            while(True):
                if(count<self.semaphor):
                    break   
            if(count<self.semaphor):
                print("process ",i," resource allocated")
                self.semaphor-=count
                sleep(10)
                print("\nprocess ",i," Process completed! Releasing the resources")
                self.semaphor+=count
                
                

#take the available resources
noOfAvailableResources=int(input("Enter the number of availbale resources: "))
obj=Semaphor(noOfAvailableResources)
print("Semaphor value: ",obj.semaphor)
#take the number of processes
noOfProcesses=int(input("Enter the number of Processs: "))
#take the resource requirements
lst=[]
for i in range(0,noOfProcesses):
    print("Enter resource requirement for process ",i+1,":")
    temp=int(input())
    lst.append(temp)
tem=[]    
#start the processes
for i in range(0,noOfProcesses):
    process=Thread(target=obj.requestResource,args=(lst[i],i+1))
    process.start()
    sleep(4)#for clear output
    tem.append(process)

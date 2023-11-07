data=[12,65,98,78,43,3,90,78,123,23,76]
max1=data[0]
min1=data[0]
for i in range(1,len(data)):
    if(max1<data[i]):
        max1=data[i]
    elif(min1>data[i]):
        min1=data[i]
print("maximum is",max1)    
print("minimum is",min1)    


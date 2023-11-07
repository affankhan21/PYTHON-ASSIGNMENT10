data=[12,23,56,81,20,23,89,20,85]
start=0
end=len(data)-1
while(start<end):
    data[start],data[end]=data[end],data[start]
    start+=1
    end-=1
print(data)    


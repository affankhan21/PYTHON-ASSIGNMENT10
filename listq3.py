data=[12,65,98,78,43,90,78,23,76]
f_max=data[0]
s_max=data[0]
for i in range(1,len(data)):
    if(f_max<data[i]):
        s_max=f_max
        f_max=data[i]
    elif(s_max<data[i]):
        s_max=data[i]
print(f_max,s_max)            
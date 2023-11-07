data=[12,23,56,89,81,20,23,89,20,85]
print(len(data))
flist=[]
for i in data:
    if i not in flist:
        flist.append(i)
data=flist
print(data)        
print(len(data))
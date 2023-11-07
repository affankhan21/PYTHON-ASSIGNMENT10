ele=int(input("ENTER THE ELEMENT YOU WANT TO REMOVE:"))
data=[12,23,56,89,81,20,23,89,20,85]
print(len(data))
for i in data:
    if i==ele:
        data.remove(i)
print((data))
print(len(data))
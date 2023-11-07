m=int(input("ENTER THE NUMBER TO CHECK FOR DIVISIBILITY :"))
n=int(input("ENTER THE NUMBER TO CHECK FOR DIVISIBILITY :"))
data=[12,23,56,89,81,20,23,89,20,85]
newl=[]
for i in data:
    if (i%m==0) and (i %n==0):
        print(i)
        newl.append(i)
print(data)
print(newl)        
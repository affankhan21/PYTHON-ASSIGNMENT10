data=[12,23,56,81,20,23,89,20,85]
ele=int(input("ENTER THE NUMBER TO SEARCH:"))
cnt=0
for i in range(0,len(data)):
    if ele ==data[i]:
        cnt+=1
else:
    if(cnt==0):
        print("element not present")    
print("count is :",cnt)       

      
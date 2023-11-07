n=int(input("ENTER THE NUMBER OF ELEMENTS YOU WANT IN THE LIST  :"))
newl=[]
even=[]
odd=[]
for i in range(0,n):
    i=int(input("enter element:"))
    newl.append(i)
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print(" TOTAL LIST OF ALL ELEMENTS ",newl) 
print("EVEN NUMBERS LIST IS: ",even)
print(" ODD NUMBER LIST IS",odd)   
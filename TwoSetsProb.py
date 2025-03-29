

arr=[2,6]
brr=[24,36]

x=min(arr)
y=max(brr)

print(y)

count=0

factor1=[]

for i in range(x,y+1):
   if (i%ele ==0 for ele in arr) :

       factor1.append(i)
       #print(f"the  factors are " , i)


for i in factor1:
    if (ele % i==0 for ele in brr):
        print(i)
        count=count+1








print(count)
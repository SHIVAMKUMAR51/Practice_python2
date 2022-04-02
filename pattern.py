
input= int(input("enter max. no. of * in first line: "))
max = 2*input
mid = max/2
min = 0
input = 2*input
for i in range(1,input):
    for j in range(1,input):
        if(i<mid):
            if(((i%2 == 0 and j%2 ==0) or (i%2 !=0 and j%2 !=0)) and (j<=max-i and j>=min+i)):
                print("*",end = "")
            else:
                print(" ",end = "")
        else:
            if(((i%2 == 0 and j%2 ==0) or (i%2 !=0 and j%2 !=0)) and (j>=max-i and j<=min+i)):
                print("*",end = "")
            else:
                print(" ",end = "")
        
    print()


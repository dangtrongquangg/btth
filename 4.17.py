n= int(input("Nhap N= "))
for i in range(2,n):
       s=0
       for j in range(1,i):
           if(i%j == 0):
              s=s+j
       if(s>i):
          print(i)

def factorial(n):
    f=1
    while (n>1):
        f=f*n
        n=n-1
    return f
def ncr(n,r):
    return int(factorial(n)/(factorial(n-r)*factorial(r)))
n=int(input("Nhap n: "))
print(" n dong cua tam giac pascal: ");
for i in range(0,n+1):
   for j in range(0,n-i+1):
      print("",end=" ")
   for j in range(i+1):
      print("{:<3}".format(ncr(i,j)), end="")
   print("")

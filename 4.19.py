p=tuple()
for i in range(1,100):
    dem=0
    for j in range(1,i+1):
        if(i%j==0):
            dem=dem+1
    if(dem==2):
        p=p+(i,)
print(p)
#vì 1 triệu khá dài và lâu nên em làm đến 100

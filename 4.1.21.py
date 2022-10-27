value=[]
items=[x for x in input("nhap cac so nhi phan: ").split(',')]
for p in items:
    intp=int(p,2)
    if not intp%5:
        value.append(p)
print('cac so nhi phan chia het cho 5 la: ',','.join(value))

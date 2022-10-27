def show(s):
    count_upper=0
    count_lower=0
    for c in s:
        if c.isupper():
            count_upper+=1
        if c.islower():
            count_lower+=1
    print("Given string:",s)
    print("chu hoa la:",count_upper)
    print("chu thuong la:",count_lower)
s=str(input())
show(s)

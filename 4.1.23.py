s=input()
d={"DIGITS":0,"LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print("so chu cai la:",d["LETTERS"])
print("so chu so la:",d["DIGITS"])

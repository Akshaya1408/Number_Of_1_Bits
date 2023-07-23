def oneBits(num):
    count=0
    while num>0:
        if num&1:
            count+=1
        num>>=1
    return count

num=int(input())
print(oneBits(num))
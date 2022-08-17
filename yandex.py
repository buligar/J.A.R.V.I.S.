a=int(input())
count=int()
c=0
if a<10000 or a==10000:
    for c in range(200):
        b = input().split()
        if b[0]=='+' and b[1].isnumeric() and b[2].isalpha():
            d=int(b[1])*b[2]
            e=str()
            e=e+d
            b1=b[2]
        prov=input().split()
        if prov[0]==('?') and prov[1].isalpha():
            c=c+1
            print(len(e))
            print(len(d))
            if len(e) >= len(d):
                print(b[2])
            else:
                print(b1)

a, b, c = [int(i) for i in input().split(" ")]
if(a>b and b<=c):
    print(":)")
elif(a<b and b>=c):
    print(":(")
elif(a<b and b<c and (c-b)<(b-a)):
    print(":(")
elif(a<b and b<c and (c-b)>=(b-a)):
    print(":)")
elif(a>b and b>c and (c-b)>(b-a)):
    print(":)")
elif(a>b and b>c and (c-b)<=(b-a)):
    print(":(")
elif(a==b and b<c):
    print(":)")
else:
    print(":(")

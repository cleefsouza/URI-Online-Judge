t = [int(i) for i in input().split(" ")]
t.sort()
if(t[0]+t[1]>t[2]):
    print("S")
elif(t[0]+t[2]>t[3]):
    print("S")
elif(t[1]+t[2]>t[3]):
    print("S")
else:
    print("N")

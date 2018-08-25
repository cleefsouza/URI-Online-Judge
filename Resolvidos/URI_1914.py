for i in range(int(input())):
    n = [str(i) for i in input().split(" ")]
    x,y = [int(i) for i in input().split(" ")]
    if((x+y)%2==0 and n[1]=="PAR"):
        print(n[0])
    elif((x+y)%2!=0 and n[1]=="IMPAR"):
        print(n[0])
    else:
        print(n[2])

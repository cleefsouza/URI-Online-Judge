class patinho:
    num = 0
    while(num!=-1):
        num = int(input())
        if(num==0):
            num = 0
            print(num)
        elif(num>=1 and num<=pow(10,19)):
            num = num-1
            print(num)
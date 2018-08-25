def fatorial(n):
    if(n==0 or n ==1):
        return 1
    else:
        return(fatorial(n-1)*n)

print(fatorial(int(input())))

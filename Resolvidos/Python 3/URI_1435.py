while True:
    try:
      n = int(input())
      if n == 0:
        break
      for i in range(1,n+1):
        for j in range(1,n+1):
          x = i
          if(j < x):
            x = j
          if(n-i+1 < x):
            x = n-i+1
          if(n-j+1 < x):
            x = n-j+1
          if j+1==n+1:
            print(" %2d"%x,end="")
          else:
            print(" %2d"%x,end=" ")
          if(j < n):
            print(end="")
          else:
            print()
      print()        

    except:
        break

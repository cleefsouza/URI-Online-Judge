x = float(input())
x = str("%.4E"%x)
if(x[0]=="-"):
  print(x)
else:
  print("+"+x)
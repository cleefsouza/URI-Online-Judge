n = input()
cen = {'0':'', '1':'C', '2':'CC', '3':'CCC', '4':'CD', '5':'D', '6':'DC', '7':'DCC', '8':'DCCC', '9':'CM'}
dez  = {'0':'', '1':'X', '2':'XX', '3':'XXX', '4':'XL', '5':'L', '6':'LX', '7':'LXX', '8':'LXXX', '9':'XC'}
uni = {'0':'', '1':'I', '2':'II', '3':'III', '4':'IV', '5':'V', '6':'VI', '7':'VII', '8':'VIII', '9':'IX'}

x = int(n)
if(x>=100):
  print(cen[n[0]]+dez[n[1]]+uni[n[2]])
elif(x<100 and x>=10):
  if(n[0]=="0"):
    n = n[1::]
  print(dez[n[0]]+uni[n[1]])
elif(x<10):
  print(uni[str(x)])

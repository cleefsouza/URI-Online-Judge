for i in range(1,int(input())+1):
  s,r = [str(i) for i in input().split(" ")]
  l = ['Bazinga!', 'Raj trapaceou!', 'De novo!']
  if(s=="tesoura" and r=="papel"):
    print("Caso #{}: {}".format(i,l[0]))
  elif(s=="papel" and r=="pedra"):
    print("Caso #{}: {}".format(i,l[0]))
  elif(s=="pedra" and r=="lagarto"):
    print("Caso #{}: {}".format(i,l[0]))
  elif(s=="lagarto" and r=="Spock"):
    print("Caso #{}: {}".format(i,l[0]))
  elif(s=="Spock" and r=="tesoura"):
    print("Caso #{}: {}".format(i,l[0]))
  elif(s=="lagarto" and r=="papel"):
    print("Caso #{}: {}".format(i,l[0]))
  elif(s=="papel" and r=="Spock"):
    print("Caso #{}: {}".format(i,l[0]))
  elif(s=="Spock" and r=="pedra"):
    print("Caso #{}: {}".format(i,l[0]))
  elif(s=="pedra" and r=="tesoura"):
    print("Caso #{}: {}".format(i,l[0]))
  elif(s=="tesoura" and r=="lagarto"):
    print("Caso #{}: {}".format(i,l[0]))
  elif(s==r):
    print("Caso #{}: {}".format(i,l[2]))
  else:
    print("Caso #{}: {}".format(i,l[1]))
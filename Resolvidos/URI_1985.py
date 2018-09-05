dic = {1001:1.50, 1002:2.50, 1003:3.50, 1004:4.50, 1005:5.50}
x = 0
for i in range(int(input())):
  p, q = [int(i) for i in input().split()]
  x+=(dic[p]*q)
print("{:.2f}".format(x))
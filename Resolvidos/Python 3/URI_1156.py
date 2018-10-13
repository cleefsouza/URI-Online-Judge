s = 1
j=2
for i in range(3, 100, 2):
    s += i/j
    j+=j
print("{:.2f}".format(s))

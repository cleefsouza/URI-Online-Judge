x = int(input())

while(x >= 1):
    palavra = input()
    tempo = len(palavra) * 0.01

    print('{:.2f}'.format(tempo))
    x -= 1

while True:
    x = int(input())
    if(x==0):
        break
    else:
        pilha = []
        discartada = []
        for x in range(1,x+1):
            pilha.append(str(x))
        
        pilha.reverse()
        while(len(pilha)>1):
            discartada.append(str(pilha[-1]))
            pilha.pop()
            pilha.insert(0, pilha[-1])
            pilha.pop()
            
            if(len(pilha)==1):
                r = pilha[0]
                print('Discarded cards:', ', '.join(discartada))
                print('Remaining card:', r)
                break
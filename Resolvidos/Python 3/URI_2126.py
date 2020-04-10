caso = 1
while True:
    try:
        subseq = input()
        string = input()

        print('Caso #{}:'.format(caso))

        qtdSubseq = string.count(subseq)

        if(qtdSubseq <= 0):
            print('Nao existe subsequencia')
        else:
            pos = string.rfind(subseq)

            print('Qtd.Subsequencias: {}'.format(qtdSubseq))
            print('Pos: {}'.format(int(pos) + 1))

        caso += 1; print()
    except EOFError:
        break

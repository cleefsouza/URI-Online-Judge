while True:
    try:
        valores = input().split(' ')

        if(valores.count('0') == 2):
            break
        else:
            valor, pago = int(valores[0]), int(valores[1])
            notas = [100, 50, 20, 10, 5, 2]
            troco = pago - valor
            possivel = False

            for nota in notas:
                trocoAux = troco - nota
                if(notas.count(trocoAux) > 0):
                    possivel = True

            if(possivel):
                print('possible')
            else:
                print('impossible')
    except EOFError:
        break

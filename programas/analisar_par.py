b = int(input('Entre com o primeiro valor: '))
c = int(input('Entre com o segundo valor: '))

resto_b = b % 2
resto_c = c % 2
#if(resto_b == 0 or not resto_c > 0):
if(resto_b == 0 or resto_c == 0):
    print('foi digitado um número par')
else:
    print('nenhum número par foi digitado')
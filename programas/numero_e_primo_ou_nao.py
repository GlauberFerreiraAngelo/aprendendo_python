numero = int(input('Entre com o número: '))

div = 0

for x in range(1, numero+1):
    resto = numero % x
    print(numero, resto)
    if (resto == 0):
        div = div + 1

if(div == 2):
    print('número {} é primo' .format(numero))
else:
    print('número {} não é primo' .format(numero))
nota_1 = int(input('Primeiro bimestre: '))
while(nota_1 > 10):
    nota_1 = int(input('Nota inválida. Entre com a nota correta: '))

nota_2 = int(input('Segundo bimestre: '))
while(nota_2 > 10):
    nota_2 = int(input('Nota inválida. Entre com a nota correta: '))

nota_3 = int(input('Terceiro bimestre: '))
while(nota_3 > 10):
    nota_3 = int(input('Nota inválida. Entre com a nota correta: '))

nota_4 = int(input('Quanto bimestre: '))
while(nota_4 > 10):
    nota_4 = int(input('Nota inválida. Entre com a nota correta: '))

media = (nota_1 + nota_2 + nota_3 + nota_4)/4

print('media: {}' .format(media))
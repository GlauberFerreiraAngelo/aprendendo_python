nota_1 = int(input('Primeiro bimestre: '))
if(nota_1 > 10):
    nota_1 = int(input('você digito errado. Primeiro bimestre: '))

nota_2 = int(input('Segundo bimestre: '))
if(nota_2 > 10):
    nota_2 = int(input('você digito errado. Segundo bimestre: '))

nota_3 = int(input('Terceiro bimestre: '))
if(nota_3 > 10):
    nota_3 = int(input('você digito errado. Terceiro bimestre: '))

nota_4 = int(input('Quanto bimestre: '))
if(nota_4 > 10):
    nota_4 = int(input('você digito errado. Quanto bimestre: '))

media = (nota_1 + nota_2 + nota_3 + nota_4)/4

if nota_1 <= 10 and nota_2 <= 10 and nota_3 <= 10 and nota_4 <= 10 :
    print('media: {}' .format(media))
else:
    print('foi informada alguma nota errada')
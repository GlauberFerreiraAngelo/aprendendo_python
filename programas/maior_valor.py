a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

print('if verificar se o valor de a ou b é o maior: ')
if(a > b):
    print('O maior número é {}' .format(a))
else:
    print('O maior número é {}' .format(b))

print('if verificar se o valor de a, b ou c é o maior: ')
if(a > b and a > c):
    print('O maior número é {}' .format(a))
elif(b > a and b > c):
    print('O maior número é {}' .format(b))
else:
    print('O maior número é {}' .format(c))
    
print('final do programa')
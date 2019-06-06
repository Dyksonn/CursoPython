from math import hypot
while True:
    try:
        co = float(input('Cumprimento do cateto oposto: '))
        ca = float(input('Cumprimento do cateto adjacente: '))
        print(f'A hipotenusa vai medir {hypot(co, ca):.2f}')
        break
    except ValueError:
        print('Valor não identificado')
        novo = str(input('Deseja fazer novamente? (s/n)')).lower()
        if novo in 'S s sim':
            continue
        else:
            break

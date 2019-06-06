from math import radians, cos, sin, tan


def titulo(txt):
    tam = len(txt)
    print()
    print('=' * tam)
    print(txt)
    print('=' * tam)


titulo('SENO, COSSENO, TANGENTE')
print()
angulo = float(input('Digite o ângulo que deseja: '))
print()
print(f'O ângulo de {int(angulo)} tem o SENO de {sin(radians(angulo)):.2f}')
print('=' * 40)
print(f'O ângulo de {int(angulo)} tem o COSSENO de {cos(radians(angulo)):.2f}')
print('=' * 40)
print(
    f'O ângulo de {int(angulo)} tem o TANGENTE de {tan(radians(angulo)):.2f}')

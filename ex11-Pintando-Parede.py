larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
print(
    f'Sua parede tem a dimensão de {larg} x {alt} e sua área é de {larg*alt:.2f}m².')
print(
    f'Para pintar essa parede, você precisa de {(larg*alt)/2:.2f}L de tinta.')

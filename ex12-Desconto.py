pro = float(input('Qual é o preço do produto? R$ '))
print(f'O produto que custava R${pro:.2f},', end=' ')
print(f'Na PROMOÇÃO com desconto de 5%, vai custar R${pro-(pro*5/100):.2f}')

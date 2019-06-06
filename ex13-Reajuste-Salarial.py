salario = float(input('Qual é o salário do Funcionário? R$ '))
print(f'Um funcionário que ganhava R$ {salario},', end=' ')
print(
    f'Com desconto de 15%, de aumento passa ganhar R$ {salario+(salario*15/100)}')

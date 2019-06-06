# ############ Operadores Aritméticos ##############

# Operadores em Python especificados
# ** Potência
# // Divisão Inteira
# % Resto da Divisão
# == Igualdade
# pow() Pode ser usado para potência

# ############# ORDEM DE PRECEDÊNCIA ############
# 1 = () Primeiro executa o que tiver entre parenteses para expressões
# 2 = ** Potência e a segunda ser executada
# 3 = *, /, //, % São o terceiro a ser executados
# 4 = +, - (São os ultimos a ser executados)

# ########### Funções de alinhamento #########
# {:20} : escrever em 20 espaços
# {:>20} alinhar a direita em espaços
# {:<20} alinhar a esquerda em espaços
# {:^20} centralizar dentro de espaços
# {:=^20} colocando simbolo igual nos espaços

# ############ Quebras de linhas em print ##########
# end='' = Pode juntar dois print na mesma linha
# \n = Essa função quebra a linha ou uma frase do print aonde deseja

# ########### Prática ##############
nome = input('Qual seu nome? ')
print('Prazer em te conhecer {:=^20}!'.format(nome))

print()

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é %s, o produto é %s e a divisão é %.3f' %
      (s, m, d), end=' ')
print('Divisão inteira %s e potência %s' % (di, e))

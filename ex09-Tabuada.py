'''num = int(input('Digite um número para ver sua tabuada: '))
print('-'*12)
print('%s x %s = %s' %(num, 1 , num*1))
print('%s x %s = %s' %(num, 2 , num*2))
print('%s x %s = %s' %(num, 3 , num*3))
print('%s x %s = %s' %(num, 4 , num*4))
print('%s x %s = %s' %(num, 5 , num*5))
print('%s x %s = %s' %(num, 6 , num*6))
print('%s x %s = %s' %(num, 7 , num*7))
print('%s x %s = %s' %(num, 8 , num*8))
print('%s x %s = %s' %(num, 9 , num*9))
print('%s x %s = %s' %(num, 10 , num*10))
print('-'*12)'''

tab = int(input('Digite um número para ver sua tabuada: '))
print("-"*12)
x = 1
while x <= 10:
    print('{0} X {1:>2} = {2:>2}'.format(tab, x, tab * x))
    x = x + 1
print("-"*12)

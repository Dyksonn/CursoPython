av1 = float(input('Qual sua nota da AV1? '))
av2 = float(input('Qual sua nota da AV2? '))
média = (av1 + av2) / 2
print('Sua da nota da AV1 %s é a nota da AV2 %s sua média e %s' %
      (av1, av2, média))
if 6 > média >= 6.9:
    print('Aluno em RECUPERAÇÃO.')
elif média < 5:
    print('Aluno está REPROVADO.')
elif média >= 7:
    print('Aluno está APROVADO.')

mae = int(input())
filho = int(input())
filhoA = int(input())

idade = filho + filhoA
filhos = mae - idade

maior = (filho + filhoA + abs((filho - filhoA)))/2
maiorAB = (filhos + maior + abs((filhos - maior)))/2

print('%d' % maiorAB)

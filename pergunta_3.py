import json


f = open('dados.json')


data = json.load(f)

dias_uteis = []
for i in data['faturamento_mensal']:

    if i['dia_util'] == True:
        dias_uteis.append(i['faturamento'])


f.close()
#print(dias_uteis)

maior = 0
menor = 999999999
soma = 0
for i in dias_uteis:

    if i > maior:
        maior = i
    if i < menor:
        menor = i
    soma = soma + i

media = soma / len(dias_uteis)

print("Maior faturamento do mês: " + str(maior))
print("Menor faturamento do mês: " + str(menor))
print("Média de faturamento do mês: " + str(media))

dias_acima_da_media = 0
for i in dias_uteis:

    if i > media:
        dias_acima_da_media = dias_acima_da_media + 1

print("Dias com faturamento acima da média: " + str(dias_acima_da_media))
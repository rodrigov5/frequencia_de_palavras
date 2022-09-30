import pandas as pd
import csv



data = pd.read_excel("debate_band.xlsx", usecols='F')

palavras = ''
for i in data["Texto"]:
    palavras = palavras + i

listaPalavras = palavras.split() # separa cada palavra presente no texto em uma lista = ['palavraExemplo', 'palavraExemplo', 'palavraExemplo']

palavrafreqs = [0,0,0]
for plvs in listaPalavras:
    if plvs == 'voto':
        palavrafreqs[0] += 1
    if plvs == 'candidato':
        palavrafreqs[1] += 1
    if plvs == 'governo':
        palavrafreqs[2] += 1


colunas = ['Palavra', 'Frequência']

linhas = [
    ['Voto', palavrafreqs[0]],
    ['Candidato', palavrafreqs[1]],
    ['Governo', palavrafreqs[2]]
]

with open('frequencias.csv', 'w', newline="") as f:
    write = csv.writer(f, delimiter=";")
    write.writerow(colunas)
    write.writerows(linhas)



        




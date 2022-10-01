import pandas as pd
import csv, string



data = pd.read_excel("debate_band.xlsx", usecols='F')

# Pega todos o texto e coloca numa unica string
palavras = ''
for i in data["Texto"]:
    palavras = palavras + i

# separa cada palavra presente no texto em uma lista = ['palavraExemplo', 'palavraExemplo', 'palavraExemplo'] e colocar e lowercase
listaPalavras = palavras.lower().split() 

# captura a frequencia das palavras e adiciona na lista
palavrafreqs = []
for p in listaPalavras:
    palavrafreqs.append(listaPalavras.count(p))





colunas = ['Palavra', 'Frequência']

linhas = list(zip(listaPalavras, palavrafreqs))

with open('frequencias.csv', 'w', newline="") as f:
    write = csv.writer(f, delimiter=";")
    write.writerow(colunas)
    write.writerows(linhas)



        




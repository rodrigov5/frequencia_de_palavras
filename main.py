import pandas as pd
import csv, string



data = pd.read_excel("debate_band.xlsx", usecols='F')


palavras = ''
for i in data["Texto"]:
    palavras = palavras + i

palavras.lower()
listaPalavras = palavras.split() # separa cada palavra presente no texto em uma lista = ['palavraExemplo', 'palavraExemplo', 'palavraExemplo']


palavrafreqs = []
for p in listaPalavras:
    palavrafreqs.append(listapalavras.count(p))





colunas = ['Palavra', 'Frequência']

linhas = [str(list(zip(listaPalavras, palavrafreqs)))]

with open('frequencias.csv', 'w', newline="") as f:
    write = csv.writer(f, delimiter=";")
    write.writerow(colunas)
    write.writerows(linhas)



        




import csv
import json

""" TRUE MP
dados = []
with open('TrueNews.txt', mode='r') as f:
    for line in f:
        dados.append(json.loads(line.strip()))

print(type(dados[0]))
print(dados[0]['title'])
"""

dados = []
with open('Historico_de_materias.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        dados.append(row['titulo'])




# open the file in the write mode
with open('true2.csv', 'w') as f:
    # create the csv writer
    writer = csv.writer(f, delimiter=';')

    writer.writerow(['title', 'rating'])
    # write a row to the csv file
    for element in dados:
        writer.writerow([element.replace(';', ','), 'verdadeiro'])

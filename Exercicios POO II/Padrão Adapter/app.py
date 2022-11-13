from JSONParser import JSONParser
from CSVAdapter import CSVAdapter

from os import path


json = JSONParser(path.join('Exercicios POO II', 'Padrão Adapter', 'files', 'example.json'))
csv = CSVAdapter(path.join('Exercicios POO II', 'Padrão Adapter', 'files', 'example.csv'))

print(json.parse())
print(csv.parse())
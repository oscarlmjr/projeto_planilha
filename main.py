# https://pypdf2.readthedocs.io/en/3.0.0/

from pathlib import Path
from PyPDF2 import PdfReader
import csv
from pathlib import Path


PASTA_RAIZ = Path(__file__).parent
PASTA_EXTRATO = PASTA_RAIZ / 'pdfs_extrato'
PASTA_NOVA = PASTA_RAIZ / 'extratos_novos'

EXTRATO_BANCARIO = PASTA_EXTRATO / 'Pasta_testexlsx.pdf'

PASTA_NOVA.mkdir(exist_ok=True)

# CAMINHO_CSV = Path(__file__).parent / 'planilhas' / 'main_2.csv'
# CAMINHO_CSV = Path(__file__).parent / 'planilhas'


reader = PdfReader(EXTRATO_BANCARIO)

# print(len(reader.pages))
# print(reader.pages)

page0 = reader.pages[0]
# page1 = reader.pages[1]

print(page0.extract_text())
# print(page1.extract_text())
print()

for linha in page0.extract_text():
    print(linha)

# print(CAMINHO_CSV)

# with open(CAMINHO_CSV, 'r', encoding='utf-8') as arquivo:
#     leitor = csv.DictReader(arquivo)
#     # leitor = csv.reader(arquivo)
#     # print(next(leitor))
#     # print(next(leitor))
#     # print(next(leitor))

#     for linha in leitor:
#         # print(linha)
#         # print(linha[0])
#         # print(linha[1])
#         # print(linha[2])
#         # print(linha['Nome'])
#         print(linha['Nome'], linha['Idade'], linha['Endereço'])


# lista_clientes = [
#     {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
#     {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
#     {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'}
# ]

# with open(CAMINHO_CSV, 'w') as arquivo:
#     nome_colunas = ['Nome', 'Endereço']
#     # nome_colunas = lista_clientes[0].keys()
#     escritor = csv.writer(arquivo)

#     escritor.writerow(nome_colunas)

#     for cliente in lista_clientes:
#         escritor.writerow(cliente.values())
#         print(cliente.values())

# # print(lista_clientes[0])
# # print(lista_clientes[0].keys())


# lista_clientes = [
#     {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
#     {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
#     {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'}
# ]


# with open(CAMINHO_CSV, 'w') as arquivo:
#     nome_colunas = lista_clientes[0].keys()
#     escritor = csv.DictWriter(
#         arquivo,
#         fieldnames=nome_colunas
#         )
#     escritor.writeheader()

#     for cliente in lista_clientes:
#         print(cliente)
#         escritor.writerow(cliente)

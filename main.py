from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger


PASTA_RAIZ = Path(__file__).parent
PASTA_EXTRATO = PASTA_RAIZ / 'pdfs_extrato' / '2025' / '11.2025'
PASTA_NOVA = PASTA_RAIZ / 'extratos_novos'

EXTRATO_BANCARIO = PASTA_EXTRATO / 'Banco do Brasil.pdf'

PASTA_NOVA.mkdir(exist_ok=True)


reader = PdfReader(EXTRATO_BANCARIO)

page0 = reader.pages[0]
# imagem0 = page0.images[0]

for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(PASTA_NOVA / f'page{i}.pdf', 'wb') as arquivo:
        writer.add_page(page)
        writer.write(arquivo)


files = [
    PASTA_NOVA / 'page1.pdf',
    PASTA_NOVA / 'page0.pdf',
]

merger = PdfMerger()
for file in files:
    merger.append(file)
    
merger.write(PASTA_NOVA / 'MERGED.pdf')
merger.close()

# for i, page in enumerate(reader.pages):
#     writer = PdfWriter()
#     with open(PASTA_NOVA / f'page{i}.pdf', 'wb') as arquivo:
#         writer.add_page(page)
#         writer.write(arquivo)

# writer = PdfWriter()

# with open(PASTA_NOVA / 'NOVO_PDF.pdf', 'wb') as arquivo:
# 	for page in reader.pages:
# 		writer.add_page(page0)
# 	writer.write(arquivo)

# writer.add_page(page0)

# with open(PASTA_NOVA / 'page0.pdf', 'wb') as arquivo:
# 	writer.write(arquivo)

# with open(PASTA_NOVA / imagem0.name, 'wb') as fp:
#     fp.write(imagem0.data)

# with open(PASTA_NOVA / page0.images[0].name, 'wb') as imagem:
    # imagem.writte()

# print(page0.images[0])
# print(len(page0.images))
# print(page0.images)
# print(page0.extract_text())
# print(len(reader.pages))

# for page in reader.pages:
#     print(page)

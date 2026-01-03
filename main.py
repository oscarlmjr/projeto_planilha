from pathlib import Path
from PyPDF2 import PdfReader


PASTA_RAIZ = Path(__file__).parent
PASTA_EXTRATO = PASTA_RAIZ / 'pdfs_extrato' / '2025' / '11.2025'
PASTA_NOVA = PASTA_RAIZ / 'extratos_novos'

EXTRATO_BANCARIO = PASTA_EXTRATO / 'Banco do Brasil.pdf'

PASTA_NOVA.mkdir(exist_ok=True)


reader = PdfReader(EXTRATO_BANCARIO)

page0 = reader.pages[0]
imagem0 = page0.images[0]

with open(PASTA_NOVA / imagem0.name, 'wb') as fp:
    fp.write(imagem0.data)

# with open(PASTA_NOVA / page0.images[0].name, 'wb') as imagem:
    # imagem.writte()

# print(page0.images[0])
# print(len(page0.images))
# print(page0.images)
# print(page0.extract_text())
# print(len(reader.pages))

# for page in reader.pages:
#     print(page)

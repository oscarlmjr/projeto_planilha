# https://pypdf2.readthedocs.io/en/3.0.0/

from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter


PASTA_RAIZ = Path(__file__).parent
PASTA_EXTRATO = PASTA_RAIZ / 'pdfs_extrato'
PASTA_NOVA = PASTA_RAIZ / 'extratos_novos'

EXTRATO_BANCARIO = PASTA_EXTRATO / 'Banco do Brasil.pdf'

PASTA_NOVA.mkdir(exist_ok=True)


reader = PdfReader(EXTRATO_BANCARIO)

# print(len(reader.pages))
# print(reader.pages)

page1 = reader.pages[1]

print(page1.extract_text())



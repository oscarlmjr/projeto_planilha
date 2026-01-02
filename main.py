from pathlib import Path
from PyPDF2 import PdfReader


PASTA_RAIZ = Path(__file__).parent
PASTA_EXTRATO = PASTA_RAIZ / 'pdfs_extrato'
PASTA_NOVA = PASTA_RAIZ / 'extratos_novos'

EXTRATO_BANCARIO = PASTA_EXTRATO / 'Banco do Brasil.pdf'

PASTA_NOVA.mkdir(exist_ok=True)



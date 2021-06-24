"""Módulo responsável pelas configurações básicas da aplicação
como, variáveis de path dos arquivos e modulos."""

import os
from pathlib import Path

# 1. Diretório base
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# 2. Planilha
DATABASE = os.path.join(BASE_DIR, 'database.xlsx')

if __name__ == '__main__':
	print(BASE_DIR)
	print(DATABASE)
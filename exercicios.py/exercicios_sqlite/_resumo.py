import sqlite3
from pathlib import Path

# Pega o arquivo
ROOT_DIR = Path(__file__).parent
DV_NAME = 'bancotext.sqlite3'
DB_FILE = ROOT_DIR / DV_NAME

# Cria uma tabela no banco de dados
TABLE_NAME = 'custumers'

# Conecta ao Banco de dados
connection = sqlite3.connect(DB_FILE)

# Executa os comandos
cursor = connection.cursor()

# Apaga tudo, mas a sequência continua
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

# Apaga tudo, e a sequência reinicia
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()


# Cria as variaveis id, name, weight
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)

# Coloca no banco de dados
connection.commit()

# Coloca as informações nas variaveis
cursor.execute(
    f'INSERT INTO {TABLE_NAME} '
    '(id, name, weight) '
    'VALUES '
    '(NULL, "Helena", 4), (NULL, "Eduardo", 10)'
)
connection.commit()


# Fecha os arquivos
cursor.close()
connection.close()
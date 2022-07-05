from bd import nova_conexao
from mysql.connector import ProgrammingError


tabela_contatos = """
    DROP TABLE CONTATOS
"""

tabela_emails = """
    DROP TABLE EMAILS
"""
try:
    with nova_conexao() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(tabela_contatos)
            cursor.execute(tabela_emails)
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
except ProgrammingError as e:
    print(f'Erro CONEXÃO: {e.msg}')
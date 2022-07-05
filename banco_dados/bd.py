from mysql.connector import connect
from contextlib import contextmanager

parametros = dict(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    auth_plugin='mysql_native_password',
    database='agenda'
)

@contextmanager
def nova_conexao():
    #unpaking do parametros do dicionario
    conexao = connect(**parametros)
    try:
        yield conexao
    finally:
        if(conexao and conexao.is_connected()):
            conexao.close()
            print('Conexao fechada')
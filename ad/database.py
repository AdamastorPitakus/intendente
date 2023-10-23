import mysql.connector 
import logging 

# Configuração do log
logging.basicConfig(level=logging.INFO)

# Configuração do banco de dados
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "Tech#2023",
    "database": "estoque"
}
# Funções de conexão
def get_connection():
    try:# Tenta estabelecer uma conexão com o banco de dados
        conn = mysql.connector.connect(**DB_CONFIG)
        logging.info("Conexão estabelecida com sucesso!")
        return conn# Retorna a conexão
    except mysql.connector.Error as err:
        logging.error(f"Erro ao conectar: {err}")
        return None# Retorna None caso ocorra um erro

def close_connection(conn):# Função para fechar a conexão
    if conn:# Verifica se a conexão existe
        conn.close()# Fecha a conexão
        logging.info("Conexão fechada com sucesso!")

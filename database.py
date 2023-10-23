import csv
import logging  # Biblioteca para adicionar logs

# Configuração básica do logging
logging.basicConfig(level=logging.INFO)

def connect_db():
    return open('products.csv', 'a+', newline='')

def close_db(connection):
    connection.close()

def insert_db(connection, produto):
    writer = csv.writer(connection)
    writer.writerow([produto.id, produto.nome, produto.descricao, produto.codigo_barras, produto.categoria, produto.preco_compra, produto.preco_venda, produto.ncm, produto.cst_icms, produto.cst_pis, produto.cst_cofins])
    logging.info(f"Produto '{produto.nome}' inserido no banco de dados.")

def select_db():
    with open('products.csv', 'r') as file:
        reader = csv.reader(file)
        return list(reader)

def update_db(produto_antigo, produto_novo):
    produtos = select_db()
    index = next((index for (index, d) in enumerate(produtos) if d[0] == produto_antigo.id), None)
    if index is not None:
        produtos[index] = [produto_novo.id, produto_novo.nome, produto_novo.descricao, produto_novo.codigo_barras, produto_novo.categoria, produto_novo.preco_compra, produto_novo.preco_venda, produto_novo.ncm, produto_novo.cst_icms, produto_novo.cst_pis, produto_novo.cst_cofins]
        with open('products.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(produtos)
        logging.info(f"Produto '{produto_antigo.nome}' atualizado para '{produto_novo.nome}' no banco de dados.")

def delete_db(produto):
    produtos = select_db()
    produtos = [p for p in produtos if p[0] != produto.id]
    with open('products.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(produtos)
    logging.info(f"Produto '{produto.nome}' excluído do banco de dados.")

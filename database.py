#arquivo database.py

import csv
import logging  # Biblioteca para adicionar logs

# Configuração básica do logging
logging.basicConfig(level=logging.INFO)

def connect_db():
    return open('products.csv', 'a+', newline='')

def close_db(connection):
    connection.close()

def get_next_id():
    produtos = select_db()
    if produtos:
        last_id = int(produtos[-1][0])
        return str(last_id + 1)
    return "1"

def insert_db(connection, produto):
    writer = csv.writer(connection)
    
    # Verifique se o arquivo está vazio
    connection.seek(0)  # Mova o cursor para o início do arquivo
    if not connection.readline():
        # Escreva o cabeçalho/título se o arquivo estiver vazio
        writer.writerow(["ID", "Nome", "Descrição", "Código de Barras", "Categoria", "Preço de Custo", "Preço de Venda", "NCM", "CST ICMS", "CST PIS", "CST COFINS"])
    
    prod_id = get_next_id()
    produto.id = prod_id
    writer.writerow([produto.id, produto.nome, produto.descricao, produto.codigo_barras, produto.categoria, produto.preco_compra, produto.preco_venda, produto.ncm, produto.cst_icms, produto.cst_pis, produto.cst_cofins])

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

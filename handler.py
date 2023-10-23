import database as db
from database import connect_db, close_db, insert_db, select_db, update_db, delete_db
from produto import Produto
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')




def input_somente_letras(prompt):
    while True:
        data = input(prompt)
        if data.isalpha():
            return data
        else:
            print("Por favor, insira apenas letras.")

def input_somente_numeros(prompt):
    while True:
        data = input(prompt)
        if data.replace(".", "").replace(",", "").isdigit():
            return float(data.replace(",", "."))
        else:
            print("Por favor, insira apenas números.")

def escolher_categoria():
    categorias = ["Uso e Consumo", "Ativo Fixo", "Revenda", "Utilização na Prestação de Serviço"]
    for idx, categoria in enumerate(categorias, 1):
        print(f"{idx}. {categoria}")
    while True:
        escolha = input("Escolha uma categoria: ")
        if escolha.isdigit() and 1 <= int(escolha) <= len(categorias):
            return categorias[int(escolha) - 1]
        else:
            print("Opção inválida. Tente novamente.")

def cadastrar_produto():
    nome = input_somente_letras("Nome do Produto: ")
    descricao = input("Descrição do Produto: ")
    codigo_barras = input_somente_numeros("Código de Barras do Produto: ")
    categoria = escolher_categoria()
    preco_custo = input_somente_numeros("Preço de Custo do Produto: ")
    preco_venda = input_somente_numeros("Preço de Venda do Produto: ")
    ncm = input("NCM do Produto (opcional): ")
    cst_icms = input("CST ICMS do Produto (opcional): ")
    cst_pis = input("CST PIS do Produto (opcional): ")
    cst_cofins = input("CST COFINS do Produto (opcional): ")
    lote = input("Lote do Produto (opcional): ")

    # Criando um objeto da classe Produto
    produto = Produto( nome, descricao, codigo_barras, categoria, preco_custo, preco_venda, ncm, cst_icms, cst_pis, cst_cofins, lote)

    conn = connect_db()
    insert_db(conn, produto)
    close_db(conn)
    print(f"Produto '{nome}' cadastrado com sucesso!")
# Função para consultar posição de estoque
def consultar_posicao_estoque():
    produtos = select_db()
    print("\n--- Consultar Posição de Estoque ---")
    print("{:<5} | {:<20} | {:<30} | {:<15} | {:<15} | {:<20} | {:<20}".format("ID", "Nome", "Descrição", "Código de Barras", "Categoria", "Preço de Custo (R$)", "Preço de Venda (R$)"))
    print("-"*110)
    for produto in produtos[1:]:
        print("{:<5} | {:<20} | {:<30} | {:<15} | {:<15} | {:<20} | {:<20}".format(*produto[:7]))

# Função para listar estoque com tributação
def listar_estoque_com_tributacao():
    produtos = select_db()
    print("\n--- Lista de Estoque com Tributação ---")
    # Aqui, você pode formatar a saída conforme necessário para mostrar os campos de tributação e o total acumulado.

# Função para adicionar produtos existente ao estoque atual
def adicionar_produtos():
    print("\n--- Adicionar Produtos ao Estoque ---")
    # Exibindo a lista de produtos antes de adicionar
    consultar_posicao_estoque()
    #recuperando os produtos do banco de dados
    produtos = select_db()

    # Escolhendo o produto a ser adicionado
    idx = int(input("Escolha o número do produto que deseja adicionar: "))
    if 0 < idx <= len(produtos):
        data = produtos[idx-1]
        produto_antigo = Produto(data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10])
        produto_antigo.id = data[0]  # ajustando o ID
        # Adicionando a quantidade
        quantidade = int(input("Quantidade a ser adicionada: "))
        produto.quantidade = quantidade
        # lotes
        lote = input("Lote do Produto (opcional): ")
        produto.lote = lote

        #antes de atualizar o produto, vamos criar uma cópia do produto antigo
        produto_antigo = Produto(data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10])
        produto_antigo.id = data[0]  # ajustando o ID

        # Atualizando o banco de dados
        conn = connect_db()
        update_db(produto_antigo, produto) # atualizando o produto
        close_db(conn)
        print(f"Produto '{produto.nome}' adicionado com sucesso!")
    else:
        print("Opção inválida!")

        
def editar_produto():
    consultar_posicao_estoque()  # usando consultar_posicao_estoque em vez de listar_produtos
    produtos = select_db()
    idx = int(input("Escolha o número do produto que deseja editar: "))
    if 0 < idx <= len(produtos):
        data = produtos[idx-1]
        produto_antigo = Produto(data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10])
        produto_antigo.id = data[0]  # ajustando o ID
        
        novo_nome = input("Novo nome do Produto: ")
        produto_novo = Produto(novo_nome, data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10])
        produto_novo.id = data[0]  # ajustando o ID
        
        update_db(produto_antigo, produto_novo)
        print("Produto atualizado com sucesso!")
    else:
        print("Opção inválida!")

def excluir_produto():
    consultar_posicao_estoque()  # usando consultar_posicao_estoque em vez de listar_produtos
    produtos = select_db()
    idx = int(input("Escolha o número do produto que deseja excluir: "))
    if 0 < idx <= len(produtos):
        data = produtos[idx-1]
        produto_a_excluir = Produto(data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10])
        produto_a_excluir.id = data[0]  # ajustando o ID
        
        delete_db(produto_a_excluir)
        print(f"Produto excluído com sucesso!")
    else:
        print("Opção inválida!")
def gerenciar_clientes():
    print("\n--- Gerenciar Clientes ---")
    # Implementação futura

def gerenciar_fornecedores():
    print("\n--- Gerenciar Fornecedores ---")
    # Implementação futura

def gerenciar_vendas():
    print("\n--- Gerenciar Vendas ---")
    # Implementação futura

def gerenciar_compras():
    print("\n--- Gerenciar Compras ---")
    # Implementação futura
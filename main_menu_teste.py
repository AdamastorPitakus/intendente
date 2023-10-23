#importa database.py
import database as db #importa database.py como db
from database import connect_db, close_db, insert_db, select_db, update_db, delete_db




# Lista de produtos para simulação
produtos = []

def main_menu():
    while True:
        # Exibe o menu principal
        print("\n--- Menu Principal ---")
        print("1 - Gerenciar Produtos")
        print("2 - Gerenciar Clientes")
        print("3 - Gerenciar Fornecedores")
        print("4 - Gerenciar Vendas")
        print("5 - Gerenciar Compras")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        # Verifica a opção escolhida
        if opcao == "1":
            gerenciar_produtos()
        elif opcao == "2":
            gerenciar_clientes()
        elif opcao == "3":
            gerenciar_fornecedores()
        elif opcao == "4":
            gerenciar_vendas()
        elif opcao == "5":
            gerenciar_compras()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

def gerenciar_produtos():
    while True:
        print("\n--- Gerenciar Produtos ---")
        print("1 - Consultar Posição de Estoque")
        print("2 - Cadastrar Produto")
        print("3 - Editar Produto")
        print("4 - Excluir Produto")
        print("0 - Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            consultar_posicao_estoque()
        elif opcao == "2":
            cadastrar_produto()
        elif opcao == "3":
            editar_produto()
        elif opcao == "4":
            excluir_produto()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

# Funções do Menu

# Adicionando os novos campos no cadastro de produtos
def cadastrar_produto():
    print("\n--- Cadastrar Produto ---")
    id = len(select_db())+1
    nome = input("Nome do Produto: ")
    descricao = input("Descrição do Produto: ")
    codigo_barras = input("Código de Barras do Produto: ")
    categoria = input("Categoria do Produto: ")
    preco_custo = input("Preço de Custo do Produto: ")
    preco_venda = input("Preço de Venda do Produto: ")
    ncm = input("NCM do Produto (opcional): ")
    cst_icms = input("CST ICMS do Produto (opcional): ")
    cst_pis = input("CST PIS do Produto (opcional): ")
    cst_cofins = input("CST COFINS do Produto (opcional): ")
    conn = connect_db()
    insert_db(conn, (id, nome, descricao, codigo_barras, categoria, preco_custo, preco_venda, ncm, cst_icms, cst_pis, cst_cofins))
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

# Função para adicionar produtos ao estoque
def adicionar_produtos():
    print("\n--- Adicionar Produtos ao Estoque ---")
    # Implementação futura
def editar_produto():
    listar_produtos()
    produtos = select_db()
    idx = int(input("Escolha o número do produto que deseja editar: "))
    if 0 < idx <= len(produtos):
        novo_nome = input("Novo nome do Produto: ")
        update_db(produtos[idx-1], novo_nome)
        print("Produto atualizado com sucesso!")
    else:
        print("Opção inválida!")

def excluir_produto():
    listar_produtos()
    produtos = select_db()
    idx = int(input("Escolha o número do produto que deseja excluir: "))
    if 0 < idx <= len(produtos):
        delete_db(produtos[idx-1])
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

if __name__ == "__main__":
    main_menu()

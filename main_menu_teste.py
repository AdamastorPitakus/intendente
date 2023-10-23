#arquivo main_menu_teste.py

import logging
import handler 
# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# criação do objeto Produto importado da classe Produto na classe construtor, deverá ser imputado
# os dados do produto para serem cadastrados no banco de dados



def main_menu():
    while True:
        print("\n--- Menu Principal ---")
        print("1 - Gerenciar Produtos")
        print("2 - Gerenciar Clientes")
        print("3 - Gerenciar Fornecedores")
        print("4 - Gerenciar Vendas")
        print("5 - Gerenciar Compras")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

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
            logging.info("Saindo do sistema.")
            break
        else:
            logging.warning("Opção inválida!")




def gerenciar_produtos():
    while True:
        print("\n--- Gerenciar Produtos ---")
        print("1 - Consultar Posição de Estoque")
        print("2 - Cadastrar NOVO Produto")
        print("3 - Editar Produto")
        print("4 - Excluir Produto")
        print("5 - adicionar produtos ao estoque existente-<importação manual>")
        print("0 - Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            handler.consultar_posicao_estoque()
        elif opcao == "2":  
            handler.cadastrar_produto()
        elif opcao == "3":
            handler.editar_produto()
        elif opcao == "4":
            handler.excluir_produto()
        elif opcao == "5":
            handler.adicionar_produtos()
        elif opcao == "0":
            logging.info("Voltando ao Menu Principal.")
            break
        else:
            logging.warning("Opção inválida!")



if __name__ == "__main__":
    main_menu()

#arquivo mainMenu


import logging
import handler
from AppProdutos import gerenciar_produtos #importa a função gerenciar_produtos da classe AppProdutos
import tkinter as tk
# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# criação do objeto Produto importado da classe Produto na classe construtor, deverá ser imputado
# os dados do produto para serem cadastrados no banco de dados



def main_menu():
    root = tk.Tk()
    app = MainMenu(root)
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



if __name__ == "__main__":
    main_menu()

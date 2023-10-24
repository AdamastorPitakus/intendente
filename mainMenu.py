import logging
import handler
from AppProdutos import gerenciar_produtos
import tkinter as tk

# Configuração do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main_menu():
    """Menu principal para gerenciamento de produtos, clientes, fornecedores, vendas e compras."""
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
            # Função gerenciar_clientes ainda não foi definida no código fornecido
            # gerenciar_clientes()
            logging.warning("Funcionalidade 'Gerenciar Clientes' ainda não implementada!")
        elif opcao == "3":
            # Função gerenciar_fornecedores ainda não foi definida no código fornecido
            # gerenciar_fornecedores()
            logging.warning("Funcionalidade 'Gerenciar Fornecedores' ainda não implementada!")
        elif opcao == "4":
            # Função gerenciar_vendas ainda não foi definida no código fornecido
            # gerenciar_vendas()
            logging.warning("Funcionalidade 'Gerenciar Vendas' ainda não implementada!")
        elif opcao == "5":
            # Função gerenciar_compras ainda não foi definida no código fornecido
            # gerenciar_compras()
            logging.warning("Funcionalidade 'Gerenciar Compras' ainda não implementada!")
        elif opcao == "0":
            logging.info("Saindo do sistema.")
            break
        else:
            logging.warning("Opção inválida!")

if __name__ == "__main__":
    main_menu()

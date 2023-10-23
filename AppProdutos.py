import logging
import handler as handler
import tkinter as tk
from tkinter import messagebox, simpledialog, messagebox, ttk
from produto import Produto
import database as db
import logging

logging.basicConfig(filename="logs.log", level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")


class AppProdutos(tk.Frame):
    def __init__(self, root):
        self.root = root
        self.root.title("Menu Interativo de Produtos")

        # Frame para visualização em tempo real
        self.preview_frame = ttk.LabelFrame(self.root, text="Pré-visualização do Produto")
        self.preview_frame.pack(pady=20, padx=20, fill="both", expand=True)
        self.preview_text = tk.StringVar()
        self.preview_label = ttk.Label(self.preview_frame, textvariable=self.preview_text)
        self.preview_label.pack(pady=10, padx=10)


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
    gerenciar_produtos()

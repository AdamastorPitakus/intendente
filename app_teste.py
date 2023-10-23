import logging
from AppProdutos import gerenciar_produtos
from main_menu_teste import main_menu as original_main_menu
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

# Configurando arquivo de log
logging.basicConfig(filename="logs.log", level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")

def modern_main_menu():
    # Primeiro, chamamos o menu original
    root_original = original_main_menu()

    # Criando uma janela com tema moderno
    root_modern = ThemedTk(theme="arc")
    root_modern.title("Menu Principal Moderno")
    root_modern.geometry("400x300")

    # Adicionando um título
    title = ttk.Label(root_modern, text="Menu Principal Moderno", font=("Arial", 24))
    title.pack(pady=20)

    # Adicionando botões
    btn_gerenciar_produtos = ttk.Button(root_modern, text="Gerenciar Produtos", command=gerenciar_produtos)
    btn_gerenciar_produtos.pack(pady=10)

    # Outros botões podem ser adicionados aqui...

    btn_sair = ttk.Button(root_modern, text="Sair", command=root_modern.quit)
    btn_sair.pack(pady=10)

    root_modern.mainloop()
    root_original.mainloop()

if __name__ == "__main__":
    modern_main_menu()

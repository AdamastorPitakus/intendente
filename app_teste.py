import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from produto import Produto
import database as db
import logging
import handler as handler
from AppProdutos import AppProdutos, gerenciar_produtos

# Configurando arquivo de log
logging.basicConfig(filename="logs.log", level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")

class MainMenu(tk.Frame):
    def open_gerenciar_produtos(self):#função para abrir o app gerenciar produtos de dentro da classe AppProdutos
        root = tk.Tk()
        app = AppProdutos(root)#chama a classe AppProdutos
        



        root.mainloop()
        gerenciar_produtos()
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("Menu PRINCIPAL")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.root.config(bg="white")
        #self.root.iconbitmap("icons/icon.ico")

        # Frame para visualização em tempo real
        self.preview_frame = ttk.LabelFrame(self.root, text="Pré-visualização do Produto")
        self.preview_frame.pack(pady=20, padx=20, fill="both", expand=True)
        self.preview_text = tk.StringVar()
        self.preview_label = ttk.Label(self.preview_frame, textvariable=self.preview_text)
        self.preview_label.pack(pady=10, padx=10)

        # MENU PRINCIPAL
        self.main_menu = ttk.LabelFrame(self.root, text="Menu Principal")
        self.main_menu.pack(pady=20, padx=20, fill="both", expand=True)

      # Botão para gerenciamento de produtos abre o AppProduto.py
        self.products_button = ttk.Button(self.main_menu, text="Gerenciar Produtos", command=self.open_gerenciar_produtos)
        self.products_button.pack(pady=20)

class AppProdutos(tk.Frame): #classe AppProdutos
        def back_to_main_menu(self):
            self.root.destroy()

def main():
        root = tk.Tk()
        app = MainMenu(root)
        root.mainloop()
        

if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenu(root)
    root.mainloop()

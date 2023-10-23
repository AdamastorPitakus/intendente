import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from produto import Produto
import database as db
import logging
import handler as handler

logging.basicConfig(filename="logs.log", level=logging.INFO, format="%(asctime)s:%(levelname)s:%(message)s")


class MainMenu(tk.Frame):
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

        # Botão para gerenciamento de produtos
        self.product_mgmt_button = ttk.Button(self.main_menu, text="Gerenciamento de Produtos", command=self.open_product_mgmt)
        self.product_mgmt_button.pack(pady=20)

    def open_product_mgmt(self):
        product_mgmt_window = tk.Toplevel(self.root)
        product_mgmt_window.title("Gerenciamento de Produtos")
        # Inicializando a classe AppProdutos dentro da nova janela
        app = AppProdutos(product_mgmt_window)




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

            # Botão para adicionar produto
            self.add_button = ttk.Button(root, text="Adicionar Produto", command=self.add_produtos)
            self.add_button.pack(pady=20)

            # Botão para listar produtos
            self.list_button = ttk.Button(root, text="Listar Produtos", command=self.list_products)
            self.list_button.pack(pady=20)

            # Botão para editar produto
            self.edit_button = ttk.Button(root, text="Editar Produto", command=self.edit_product)
            self.edit_button.pack(pady=20)

            # Botão para excluir produto
            self.delete_button = ttk.Button(root, text="Excluir Produto", command=self.delete_product)
            self.delete_button.pack(pady=20)

            # Botão para voltar ao menu principal
            self.back_button = ttk.Button(root, text="Voltar ao Menu Principal", command=self.back_to_main_menu)
            self.back_button.pack(pady=20)

        def add_produtos(self):
            try:
                # Criando uma instância da classe Produto
                product = Produto()

                # Obtendo os dados do produto
                product.name = simpledialog.askstring("Nome", "Digite o nome do produto:")
                if not product.name:
                    raise ValueError("Nome do produto é obrigatório!")

                product.price = simpledialog.askfloat("Preço", "Digite o preço do produto:")
                if not product.price:
                    raise ValueError("Preço do produto é obrigatório!")

                product.quantity = simpledialog.askinteger("Quantidade", "Digite a quantidade do produto:")
                if not product.quantity:
                    raise ValueError("Quantidade do produto é obrigatória!")

                # Adicionando o produto ao banco de dados
                handler.add_product(product)

                # Atualizando a pré-visualização
                self.update_preview(product)

                messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
            except Exception as e:
                messagebox.showerror("Erro", str(e))

        def list_products(self):
            # Obtendo todos os produtos do banco de dados
            products = handler.get_products()

            # Atualizando a pré-visualização
            self.update_preview(products)

        def edit_product(self):
            # Selecionando o produto a ser editado pode pesquisar por id, codigo ou nome
            product_id = simpledialog.askinteger("ID", "Digite o ID do produto:")
            product = handler.get_product(product_id)
            
            # Verificando se o produto existe
            if product:
                # Obtendo os novos dados do produto
                product.name = simpledialog.askstring("Nome", "Digite o nome do produto:", initialvalue=product.name)
                product.price = simpledialog.askfloat("Preço", "Digite o preço do produto:", initialvalue=product.price)
                product.quantity = simpledialog.askinteger("Quantidade", "Digite a quantidade do produto:", initialvalue=product.quantity)

                # Atualizando o produto no banco de dados
                handler.update_product(product)

                # Atualizando a pré-visualização
                self.update_preview(product)
            else:
                messagebox.showwarning("Produto não encontrado", "O produto com o ID {} não foi encontrado.".format(product_id))

        def delete_product(self):
            # Selecionando o produto a ser excluído
            product_id = simpledialog.askinteger("ID", "Digite o ID do produto:")
            product = handler.get_product(product_id)

            # Verificando se o produto existe
            if product:
                # Excluindo o produto do banco de dados
                handler.delete_product(product_id)

                # Atualizando a pré-visualização
                self.update_preview(product)
            else:
                messagebox.showwarning("Produto não encontrado", "O produto com o ID {} não foi encontrado.".format(product_id))
        
        def update_preview(self, product):
            """Atualiza a pré-visualização com os dados do produto"""
            if isinstance(product, Produto):
                self.preview_text.set("ID: {}\nNome: {}\nPreço: {}\nQuantidade: {}".format(product.id, product.name, product.price, product.quantity))
            elif isinstance(product, list):
                self.preview_text.set("Produtos: {}".format(len(product)))
            else:
                self.preview_text.set("")

        def back_to_main_menu(self):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainMenu(root)
    root.mainloop()

import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from produto import Produto

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
        App_produtos(product_mgmt_window)  # Inicializando a classe App_produtos dentro da nova janela



    class App_produtos(tk.Frame):
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
            self.add_button = ttk.Button(root, text="Adicionar Produto", command=self.add_product)
            self.add_button.pack(pady=20)

            # Botão para listar produtos
            self.list_button = ttk.Button(root, text="Listar Produtos", command=self.list_products)
            self.list_button.pack(pady=20)

            # Lista para armazenar produtos
            self.products = []

        def ask_combobox(self, title, prompt, values):
            """Função personalizada para exibir um combobox."""
            dialog = tk.Toplevel(self.root)
            dialog.title(title)
            ttk.Label(dialog, text=prompt).pack(pady=10, padx=10)
            combo_var = tk.StringVar()
            combobox = ttk.Combobox(dialog, textvariable=combo_var, values=values)
            combobox.pack(pady=10, padx=10)
            combobox.set(values[0])
            ttk.Button(dialog, text="OK", command=dialog.destroy).pack(pady=10)
            self.root.wait_window(dialog)
            return combo_var.get()

        def add_product(self):
            nome = simpledialog.askstring("Input", "Nome do Produto (Apelido ou Nome Amigável):")
            self.preview_text.set(f"Nome: {nome}")
            
            descricao = simpledialog.askstring("Input", "Descrição do Produto:")
            self.preview_text.set(self.preview_text.get() + f"\nDescrição: {descricao}")
            
            codigo_barras = simpledialog.askstring("Input", "Código de Barras (opcional):") or "000000000"
            self.preview_text.set(self.preview_text.get() + f"\nCódigo de Barras: {codigo_barras}")
            
            categoria = self.ask_combobox("Input", "Categoria:", ["Ativo Fixo", "Uso e Consumo", "Revenda", "Utilizar na Prestação de Serviços"])
            self.preview_text.set(self.preview_text.get() + f"\nCategoria: {categoria}")
            
            preco_compra = float(simpledialog.askstring("Input", "Preço de Compra:"))
            self.preview_text.set(self.preview_text.get() + f"\nPreço de Compra: R${preco_compra}")
            
            preco_venda = float(simpledialog.askstring("Input", "Preço de Venda:"))
            self.preview_text.set(self.preview_text.get() + f"\nPreço de Venda: R${preco_venda}")
            
            quantidade = float(simpledialog.askstring("Input", "Quantidade:"))
            self.preview_text.set(self.preview_text.get() + f"\nQuantidade: {quantidade}")
            
            unidade_de_medida = self.ask_combobox("Input", "Unidade de Medida:", Produto.UNIDADES_DE_MEDIDA)
            self.preview_text.set(self.preview_text.get() + f"\nUnidade de Medida: {unidade_de_medida}")

            product = Produto(nome, descricao, codigo_barras, categoria, preco_compra, preco_venda, quantidade, unidade_de_medida)
            self.products.append(product)

            messagebox.showinfo("Info", f"Produto '{nome}' adicionado com sucesso!")

        def list_products(self):
            product_list = "\n".join([str(product) for product in self.products])
            messagebox.showinfo("Lista de Produtos", product_list or "Nenhum produto adicionado.")

    if __name__ == "__main__":
        root = tk.Tk()
        app = App_produtos(root)
        root.mainloop()

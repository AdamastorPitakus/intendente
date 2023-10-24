import database as db
import logging

# Configuração básica do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Produto:
    _id = 0  # ID sequencial do sistema
    UNIDADES_DE_MEDIDA = ["Unidade", "Kg", "L", "m²", "m³", "Pacote", "Caixa", "Dúzia"]

    @classmethod
    def get_next_id(cls):
        cls._id += 1
        return cls._id

    def __init__(self, nome, descricao, codigo_barras, categoria, preco_compra, preco_venda, quantidade, unidade_de_medida, codigo_item=None, ncm=None):
        self.id = Produto.get_next_id()
        self.codigo_item = codigo_item or self.id
        self.nome = nome
        self.descricao = descricao
        self.codigo_barras = codigo_barras
        self.categoria = categoria
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.quantidade = quantidade
        self.unidade_de_medida = unidade_de_medida
        self.ncm = ncm
        self.lotes = []

        self._validar()
        logging.info(f"Produto '{self.nome}' criado com ID: {self.id} e Código do Item: {self.codigo_item}")

    def _validar(self):
        if not all([self.nome, self.descricao, self.codigo_barras, self.categoria]):
            logging.error("Todos os campos (nome, descrição, código de barras e categoria) são obrigatórios.")
            raise ValueError("Dados do produto inválidos.")
        if self.preco_compra < 0 or self.preco_venda < 0:
            logging.error("Os preços de compra e venda não podem ser negativos.")
            raise ValueError("Preço inválido.")
        if self.unidade_de_medida not in Produto.UNIDADES_DE_MEDIDA:
            logging.error(f"Unidade de medida inválida. Opções válidas: {', '.join(Produto.UNIDADES_DE_MEDIDA)}")
            raise ValueError("Unidade de medida inválida.")

    def atualizar(self, nome, descricao, codigo_barras, categoria, preco_compra, preco_venda, quantidade, unidade_de_medida, codigo_item=None, ncm=None):
        self.codigo_item = codigo_item or self.codigo_item
        self.nome = nome
        self.descricao = descricao
        self.codigo_barras = codigo_barras
        self.categoria = categoria
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.quantidade = quantidade
        self.unidade_de_medida = unidade_de_medida
        self.ncm = ncm or self.ncm

        self._validar()
        logging.info(f"Produto '{self.nome}' atualizado com ID: {self.id} e Código do Item: {self.codigo_item}")    

    def adicionar_lote(self, lote):
        self.lotes.append(lote)
        logging.info(f"Lote adicionado ao produto '{self.nome}'")

    def remover_lote(self, lote_id):
        self.lotes = [lote for lote in self.lotes if lote.id != lote_id]
        logging.info(f"Lote com ID {lote_id} removido do produto '{self.nome}'")

    def obter_quantidade_total(self):
        return sum([lote.quantidade for lote in self.lotes])

    def __str__(self):
        return f"ID: {self.id}, Código do Item: {self.codigo_item}, Nome: {self.nome}, Descrição: {self.descricao}, Código de Barras: {self.codigo_barras}, Categoria: {self.categoria}, Preço de Compra: R${self.preco_compra}, Preço de Venda: R${self.preco_venda}, Quantidade: {self.quantidade} {self.unidade_de_medida}"
    
    def save_to_db(self):
        conn = db.connect_db()
        db.insert_db(conn, self)
        db.close_db(conn)
        logging.info(f"Produto '{self.nome}' salvo no banco de dados.")

    @classmethod
    def get_all(cls):
        produtos = db.select_db()
        return [cls(*produto[1:]) for produto in produtos[1:]]

    @classmethod
    def update(cls, produto_antigo, produto_novo):
        conn = db.connect_db()
        db.update_db(conn, produto_antigo, produto_novo)
        db.close_db(conn)

    @classmethod
    def delete(cls, produto):
        conn = db.connect_db()
        db.delete_db(conn, produto)
        db.close_db(conn)

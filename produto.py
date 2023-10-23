# arquivo produto.py

import logging  # Biblioteca para adicionar logs

# Configuração básica do logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Produto:
    _id = 0  # ID inicial

    @classmethod
    def get_next_id(cls):
        cls._id += 1
        return cls._id

    def __init__(self, nome, descricao, codigo_barras, categoria, preco_compra, preco_venda, ncm=None, cst_icms=None, cst_pis=None, cst_cofins=None, lote=None):
        self.id = Produto.get_next_id()  # Gera um novo ID sequencial
        self.nome = nome
        self.descricao = descricao
        self.codigo_barras = codigo_barras
        self.categoria = categoria
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.ncm = ncm  # NCM do produto
        self.cst_icms = cst_icms  # CST ICMS do produto
        self.cst_pis = cst_pis  # CST PIS do produto
        self.cst_cofins = cst_cofins  # CST COFINS do produto
        self.lotes = []

        logging.info(f"Produto '{self.nome}' criado com ID: {self.id}")

    def adicionar_lote(self, lote):
        self.lotes.append(lote)
        logging.info(f"Lote adicionado ao produto '{self.nome}'")

    def remover_lote(self, lote_id):
        self.lotes = [lote for lote in self.lotes if lote.id != lote_id]
        logging.info(f"Lote com ID {lote_id} removido do produto '{self.nome}'")

    def obter_quantidade_total(self):
        return sum([lote.quantidade for lote in self.lotes])

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Descrição: {self.descricao}, Código de Barras: {self.codigo_barras}, Categoria: {self.categoria}, Preço de Compra: R${self.preco_compra}, Preço de Venda: R${self.preco_venda}"

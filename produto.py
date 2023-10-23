import uuid as uuid # Biblioteca para gerar o id do produto
from datetime import datetime # Biblioteca para gerar a data de validade do produto



class Produto:
    def __init__(self, id, nome, descricao, codigo_barras, categoria, preco_compra, preco_venda):
        self.id = uuid.uuid4()
        self.nome = nome
        self.descricao = descricao
        self.codigo_barras = codigo_barras
        self.categoria = categoria
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.lotes = []

    def adicionar_lote(self, lote):
        self.lotes.append(lote)

    def remover_lote(self, lote_id):
        self.lotes = [lote for lote in self.lotes if lote.id != lote_id]

    def obter_quantidade_total(self):
        return sum([lote.quantidade for lote in self.lotes])

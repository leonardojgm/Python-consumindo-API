from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tipo, tamanho):
        super().__init__(nome, preco)
        self._tipo = tipo
        self._tamanho = tamanho

    @property
    def tipo(self):
        return self._tipo

    @property
    def tamanho(self):
        return self._tamanho
    
    def aplicar_desconto(self):
        self._preco -= self._preco * 0.08
from cardapio.Item_cardapio import Cardapio


class Bebida(Cardapio):

    def __init__(self,nome,preco,tamanho):
        super().__init__(nome,preco)
        self.descricao = tamanho

    def __str__(self):
        return self._nome
    
    @property
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)
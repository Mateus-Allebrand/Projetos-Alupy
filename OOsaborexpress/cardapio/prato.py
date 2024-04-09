from cardapio.Item_cardapio import Cardapio


class Prato(Cardapio):

    def __init__(self,nome,preco,descricao):
        super().__init__(nome,preco)
        self.descricao = descricao

    def __str__(self) -> str:
        return self._nome
    
    @property
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)
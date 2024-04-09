from avaliacoes import Avaliacao
from cardapio.Item_cardapio import Cardapio



class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
            
        self.nome = nome.title()
        self.categoria = categoria.title()
        self._ativo = True
        Restaurante.restaurantes.append(self)
        self._avaliacao = []
        self._cardapio = []



    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo}'

    
    def listar_restaurantes():

        x = (f"{'Nome'.ljust(25)} | {'Categoria'.ljust(25)} | {'Média Valiação: '.ljust(25)} | {'Status'.ljust(25)}")
        print(x)
        tam = len(x)
        print(f"-" * tam)
        for restaurante in Restaurante.restaurantes:
            print(f"{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo.ljust(25)}")

    @property
    def ativo(self):
        return "✅" if self._ativo == True else "☐"

  
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente,nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        media_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(media_notas / quantidade_notas, 1)
        return media
    


    def adcionar_no_cardapio(self, item):
        if isinstance(item,Cardapio):
            self._cardapio.append(item)



    @property
    def listar_cardapio(self):
        print(f"Cardapio do Restaurante {self.nome}")
        for i,item in enumerate(self._cardapio,start=1):
            if hasattr(item, "descricao"):
                msg_prato  = (f" {i} Nome: {item._nome.ljust(22)} | Preço: R$ {str(item._preco).ljust(22)} | Descrição: {item.descricao.ljust(22)}")
                print(msg_prato)
            else:
                msgbebida  = (f"Nome: {item._nome.ljust(22)} | Preço: R$ {str(item._preco).ljust(22)} | Tamanho: {item.tamanho.ljust(22)}")
                print(msgbebida)


    # def adcionar_bebidas_restaurante(self,bebida):
    #     self._cardapio.append(bebida)


    # def adcionar_prato_restaurante(self,prato):
    #     self._cardapio.append(self,prato)





# pizza = Restaurante("pizzelli", "Italizana")

# sushi = Restaurante("sushinaga","japones")

# churrascaria = Restaurante("chucrismo", "Gaúcha")

# Restaurante.listar_restaurantes()


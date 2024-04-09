from modelos import Restaurante
from cardapio.bebida import Bebida
from cardapio.prato import Prato


def main():

    pizza = Restaurante("pizzelli", "Italizana")
    sushi = Restaurante("sushinaga","japones")
    churrascaria = Restaurante("chucrismo", "Gaúcha")
    churrascaria.receber_avaliacao("Carlos", 5)
    churrascaria.receber_avaliacao("Carlos", 10)


    bebida_suco = Bebida("suco de Melancia",10,"Grande")
    bebida_suco.aplicar_desconto
    prato_dia = Prato("alaminuta", 100, "vem com feijoada")
    prato_dia.aplicar_desconto

    churrascaria.adcionar_no_cardapio(bebida_suco)
    churrascaria.adcionar_no_cardapio(prato_dia)

    churrascaria.listar_cardapio

if __name__ == "__main__":
    main()
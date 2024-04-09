from modelos import Restaurante



def main():

    pizza = Restaurante("pizzelli", "Italizana")

    sushi = Restaurante("sushinaga","japones")

    churrascaria = Restaurante("chucrismo", "Gaúcha")

    

    churrascaria.receber_avaliacao("Carlos", 5)
    churrascaria.receber_avaliacao("Carlos", 10)


    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()
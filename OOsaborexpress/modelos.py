class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
            
        self.nome = nome.title()
        self.categoria = categoria.title()
        self._ativo = True
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo}'

    
    def listar_restaurantes():

        x = (f"{'Nome'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'.ljust(25)}")
        print(x)
        tam = len(x)
        print(f"-" * tam)
        for restaurante in Restaurante.restaurantes:
            print(f"{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo.ljust(25)}")

    @property
    def ativo(self):
        return "✅" if self._ativo == True else "☐"





# pizza = Restaurante("pizzelli", "Italizana")

# sushi = Restaurante("sushinaga","japones")

# churrascaria = Restaurante("chucrismo", "Gaúcha")

# Restaurante.listar_restaurantes()


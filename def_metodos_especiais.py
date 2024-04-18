import re


class ExtratorURL:
    def __init__(self, url):                                # existe esses metodos que possuem __ antes e __                                                     
        self.url = self.sanitiza_url(url)                   # depois, são chamados de metodos especiais
        self.valida_url()                                   #Pois (nós programadores) não chamamos eles diretamente 
                                                            #esses métodos são chamados pelo próprio Python para executar
    def sanitiza_url(self, url):                            #alguns ações específicas 
        if type(url) == str:                                #no caso de __init__, ele é chamado pelo proprio python para
            return url.strip()                              #inicializar os valores da estancia da nossa classe
        else:
            return ""
                                                            # extrator_url = ExtratorURL(url) <= como nesse caso
    def valida_url(self):                                   # nesse caso, python sabe que dentre algumas coisas que ele tem que fazer
        if not self.url:                                    # como alocar memória para esse objeto que vai ser criado, ele precisa inicializar 
            raise ValueError("A URL está vazia")            # Os valores dos atributos desse objeto para essa estancia da classe 
                                                            # É isso que o __init__  faz
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url)
        if not match:
            raise ValueError("A URL não é válida.")         #Outro exemplo é nesse caso: if type(url) == str: 
                                                            #aqui por baixo dos panos, python está chamando o método
    def get_url_base(self):                                 # __eq__  que vai comparar esses dois valores
        indice_interrogacao = self.url.find('?')          
        url_base = self.url[:indice_interrogacao]           # Outro exemplo => print(len(url))
        return url_base                                     # é o mesmo que => url.__len__()

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url


    # def __str__(self) -> str:
    #     return self.url

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"




estrator_url = ExtratorURL(url)
estrator_url2 = ExtratorURL(url)


print("O tamano da minha URL é: ",len(estrator_url))

print(estrator_url == estrator_url2) # Esta me retornando => False
                                     # pois por baixo dos panos o que acontece é isso:
                                     # estrator_url.__eq__(estrator_url2)
                                     # ele esta comparando o endereço de memória entre esses dois objetos
                                     # que obviamente não é o mesmo
                                     # Como solução, tenho que achar uma forma de comparar os atributos dessa objeto

     
# def __eq__(self, other):           # aqui no caso, o __eq__ recebe como argumento esse other
#     return self.url == other.url   # esse other no caso, é o objeto a direita da minha comparação => obj a esquerda ==obj a direita
                                     # com essa função: resolverá o problema, pois estou comparando os atributos dos objetos
                                     # def __eq__(self, other):          
                                     #     return self.url == other.url



# if estrator_url == estrator_url2:
#     print(f"{estrator_url} é igual a {estrator_url2}")

# else:
#     print(f"{estrator_url} e {estrator_url2} Não são iguais")



#com o metodo id(), eu consigo ver o endereço de memória dos objetos

print(id(estrator_url))
print(id(estrator_url2))









# extrator_url = ExtratorURL(url)
# valor_quantidade = extrator_url.get_valor_parametro("quantidade")
# print(valor_quantidade)
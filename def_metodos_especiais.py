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


    def __str__(self) -> str:
        return self.url

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
print(len(url))

# extrator_url = ExtratorURL(url)
# valor_quantidade = extrator_url.get_valor_parametro("quantidade")
# print(valor_quantidade)



estrator_url0 = 
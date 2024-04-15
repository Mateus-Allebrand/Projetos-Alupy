url = "http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

print(url)

# texto = url[0:5]
# texto02 = url.split("/")
# print(texto)
# print(texto02)


parametros_url = url.find("?")

print(url[parametros_url+1:])

nome = "Gabriel saldanha"


first_nome = nome.split(" ")

print(first_nome[0])


import re


endereco = "Rua sargento Marcos Henrique Telles Ferreira, número 207, Tarumã, cep: 94415-350"


padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
#Formas mais simples de escrever o trecho decodigo acima
#padrao = re.compile("[0123456789]{5}[-]?[0123456789]{3}")
#padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")
#padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")   
#obs: {numero} é chamado de quantificador, serve para dizer quantas vezes aquele conjuto aparacer naquele padrão
#funcionado mesmo jeito que o codigo acima, só que é bem mais simples de escrever o codigo , e até de intender






busca = padrao.search(endereco)




if busca:
    cep = busca.group()
    print(cep)



#Para estrair uma regex de uma stringo geralmente seguimos os três passos

# compilação de uma padrão
# busca de uma padrão em uma certa string 
# e se encontrar esse padrão 
# caso a busca retorne alguma coisa podemos estrair do objeto match o valor de retorno
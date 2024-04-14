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
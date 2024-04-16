import re


texto = "Rafaela Brasil, CPF: 718.457.190-85"

padrao = re.compile("[0-9]{3}[.]{0,1}[0-9]{3}[.]{0,1}[0-9]{3}[-]{0,1}[0-9]{2}")

pesquisa = padrao.search(texto)
#Metodo Search,vai procurar dentro de uma string se aquele padrão foi encontrado dentro dela

#print(pesquisa.group())



# Exemplos de URLs válidas:

# bytebank.com/cambio
# bytebank.com.br/cambio
# www.bytebank.com/cambio
# www.bytebank.com.br/cambio
# http://www.bytebank.com/cambio
# http://www.bytebank.com.br/cambio
# https://www.bytebank.com/cambio
# https://www.bytebank.com.br/cambio

# Exemplos de URLs inválidas:

# https://bytebank/cambio
# https://bytebank.naoexiste/cambio
# ht://bytebank.naoexiste/cambio




url = "https://www.bytebank.com.br/cambio" 

padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
#Tenho que lembrar de compilar a minha string

match = padrao_url.match(url)
#O metodo match verefica se a minha string é extamente igual

if not match:
    raise ValueError("Url Inválida")

else:
    print("Deu match")
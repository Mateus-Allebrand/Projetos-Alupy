import re


texto = "Rafaela Brasil, CPF: 718.457.190-85"

padrao = re.compile("[0-9]{3}[.]{0,1}[0-9]{3}[.]{0,1}[0-9]{3}[-]{0,1}[0-9]{2}")

pesquisa = padrao.search(texto)

print(pesquisa.group())
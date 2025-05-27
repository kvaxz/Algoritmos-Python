##É POSSIVEL CRIAR UM DICIONARIO DENTRO DE UMA CHAVE DE UM DICIONARIO

dados ={
    "Crossfox":{"km":35000,"ano":2005},
    "DS5":{"km":17000,"ano":2015},
    "Fusca":{"km":170000,"ano":1979},
    "Jetta":{"km":137902,"ano":2022},
    "Passat":{"km":93756,"ano":2019}
}

print(dados.get("Fusca","Veiculo Não Encontrado")) ##NÃO ENCONTRA O "GOL"

print(dados["Crossfox"]["ano"]) #PRIMEIRO OQUE EU QUERO PUXAR, DEPOIS OQUE EU QUERO PUXAR LÁ DE DENTRO
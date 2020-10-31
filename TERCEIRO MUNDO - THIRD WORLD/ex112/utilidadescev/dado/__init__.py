'''Exercício Python 112: Dentro do pacote utilidadesCeV que criamos
no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro()
que seja capaz de funcionar como a função input(),
mas com uma validação de dados para aceitar apenas valores que seja monetários.'''
def leiaDinheiro(msg):
    validar = False
    while validar == False:
        preço = str(input(msg)).strip().replace(",",".")
        if preço.isalpha() or preço == "":
            print(f"ERRO!! \"{preço}\" não é um valor")
        else:
            validar = True
            return float(preço)
        
def readInt(message):
    okay = False
    while True:
        n = str(input(message))
        if n.isnumeric():
            int(n)
            okay = True
            break
        else:
            print("ERROR!! YOU NOT WRITED A NUMBER")
    return n

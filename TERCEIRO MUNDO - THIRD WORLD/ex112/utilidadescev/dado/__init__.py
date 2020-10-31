'''Exercício Python 112: Dentro do pacote utilidadesCeV que criamos
no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro()
que seja capaz de funcionar como a função input(),
mas com uma validação de dados para aceitar apenas valores que seja monetários.'''
def leiaDinheiro(msg):
    validar = False
    while validar == False:
        preço = str(input(msg)).strip()
        if preço.isnumeric():
            float(preço)
            validar = True
        if validar == True:
            break
        else:
            print(f"ERRO!! \"{preço}\" não é um valor")

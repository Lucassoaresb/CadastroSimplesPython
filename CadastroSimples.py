from time import sleep
print("=="*22)
nome = input("Digite seu nome para iniciar o promgrama: ")
print("=="*22)
print("Olá",nome,"por favor escolha uma opção")
sair = False
while not sair:
    menu = int(input('''
    [0] SAIR DO PROGRAMA 
    [1] ENTRAR NO PROGRAMA 
    [2] FAÇA SEU CADASTRO 
    [3] MOSTRAR CADASTRO
    '''))
    if menu == 0:
        print("Você escolheu encerrar o programa...")
        sleep(2)
        print("          PROGRAMA FINALIZADO")
        sair = True
    if menu == 1:
        print("Seja bem vindo",nome)
    if menu == 2:
        id = input("Digite o seu ID de usuário: ")
        idade = input("{} digite sua idade: ".format(id))
        sleep(1)
        print('''
        Conta cadastrada com sucesso!!''')
    if menu == 3:
        print('''
    SEU ID É: {} 
    VOCÊ TEM {} ANOS'''.format(id, idade))
        sleep(2)
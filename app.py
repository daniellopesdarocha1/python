# -*- coding: UTF-8 -*-

def listar(nomes):
    print ('Listando nomes:')
    for nome in nomes:
        print (nome)


def cadastrar(nomes):
    print ('Digite o nome:')
    nome = input()
    nomes.append(nome)


def remover(nomes):
    print ('Qual nome voce gostaria de remover?')
    para_remover = input()
    if (para_remover in nomes):
        nomes.remove(para_remover)
        print ('Removido com sucesso!')
    else:
        print('Nome não encontrado.')


def alterar(nomes):
    print ('Qual nome vc gostaria de alterar?')

    #cliente deve digitar o nome a alterar
    verificar_se_nome_existe = input()

    #devemos verificar se existe esse nome na lista
    if (verificar_se_nome_existe in nomes):
        #se existir o cliente deve digitar o novo nome
        print ('Informe o novo nome:')
        alterar_nome_para = input()
        #devemos pegar a posição do nome a alterar na lista
        posicao_nome = nomes.index(verificar_se_nome_existe)
        #e colocar na posição correta o novo nome
        nomes[posicao_nome] = alterar_nome_para
        print ('%s Alterado com sucesso!' % alterar_nome_para)


def procurar(nomes):
    print ('Digite nome a procurar:')
    nome_a_procurar = input()
    #faça um if que usa o operador in
    if (nome_a_procurar in nomes):
        print ('Nome %s está cadastrado!' % nome_a_procurar)
        return 1
    else:
        print ('Nome não está cadastrado.')
        return 0


def menu():
    nomes = []
    escolha = ''
    while(escolha != '0'):
        print ('Digite: 1 Cadastrar, 2 Listar, 3 Remover, 4 Alterar, 5 Procurar, 0 Terminar')
        escolha = input()

        if (escolha == '1'):
            cadastrar(nomes)

        if (escolha == '2'):
            listar(nomes)

        if (escolha == '3'):
            remover(nomes)

        if (escolha == '4'):
            alterar(nomes)

        if (escolha == '5'):
            procurar(nomes)


menu()

# otimizando o sistema bancario com o módulo de funções
# Separar as funções de saque, depósito e visualização do extrato
# Criar funções de criar cliente e outra de criar conta corrente


"""
    Função de saque deve receber argumentos apenas por nome:
    nomes sugeridos argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques
    nomes sugeridos retorno: saldo, extrato

    Função de depósito deve receber os argumentos apenas pos posição:
    nomes sugeridos argumentos: saldo, valor, extrato
    sugestão de retornos: saldo e extrato

    Função extrato deve receber os argumentos por posição e nome:
    argumentos posicionais: saldo
    argumentos nomeados: extrato

    Criar usuário, criar conta corrente, listar contas
"""

import textwrap

def menu():
    
    menu = """\n
    $$$$$$$$$$$$$$$$$$$$$ MENU $$$$$$$$$$$$$$$$$$$$$
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    pass

    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /): # todos os elementos obrigatoriamente passados por posição, tudo antes de / exige posição
    try:
        valor = float(valor)
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n == Depósito realizado com sucesso! ==")
    except ValueError as e:
        print(f"\n ### Operação falhou! {e}")
    return saldo, extrato


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques): # por ter o * argumentos são passados obrigatoriamente de forma nomeada
    valida_excedeu_saldo = valor > saldo

    valida_excedeu_limite = valor > limite

    valida_excedeu_quantidade_saques = numero_saques >= limite_saques

    if valida_excedeu_saldo:
        print("Operação falhou! O saldo é insuficiente.")
        
    elif valida_excedeu_limite:
        print("Operação falhou! O limite de saque por operação é de {limite}.".format(limite))
        
    elif valida_excedeu_quantidade_saques:
        print("Operação falhou! O numero limite de saques diários é de {} saques.".format(limite_saques))

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n == Saque realizado com sucesso!")

    else:
        print("Operação falhou! O valor informado é invalido")

    return saldo, extrato

def gerar_extrato(saldo, /, *, extrato):
    print("\n")
    print("Extrato".center(30, "#"))
    print("\n")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("".center(30, "#"))

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("## Já existe um usuário com esse CPF! ##")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("### Usuário criado com sucesso! ###")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuarios for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)
    

    if usuario:
        print("\n Conta criada com sucesso! ")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario[0]}
    
    print("\n ### Usuário não encontrado, fluxo de criação de conta encerrado! ###")

def listar_contas(contas):
    for conta in contas:
        nome_usuario = conta['usuario'].get('nome', 'Nome não disponível')

        descricao_conta = f"""\
                Agência:\t{conta['agencia']}
                Número:\t{conta['numero_conta']}
                Titular:\t{nome_usuario}
        """
        print("#" * 40)
        print(textwrap.dedent(descricao_conta))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0726"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Infore o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

        elif opcao == "e":
            gerar_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            
            if conta:
                contas.append(conta)
                

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Opção selecionada inválida, por favor selecione novamente.")
            


main()
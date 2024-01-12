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

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500.00
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d": 
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação não realizada! O valor informado é inválido, deve ser maior que 0.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        valida_excedeu_saldo = valor > saldo

        valida_excedeu_limite = valor > limite

        valida_excedeu_quantidade_saques = numero_saques >= LIMITE_SAQUES

        if valida_excedeu_saldo:
            print("Operação não realizada! O saldo é insuficiente.")
        
        elif valida_excedeu_limite:
            print("Operação não realizada! O limite de saque por operação é de {limite}.".format(limite))
        
        elif valida_excedeu_quantidade_saques:
            print("Operação não realizada! O numero limite de saques diários é de {} saques.".format(LIMITE_SAQUES))

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação não realizada! O valor informado é invalido")
        
    
    elif opcao == "e":
        print("\n")
        print("Extrato".center(30, "#"))
        print("\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("".center(30, "#"))

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
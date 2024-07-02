menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        while True:
            valor = float(input("Digite o valor a ser depositado: "))
            if valor > 0:
                saldo += valor
                extrato += f"Depósito de R$ {valor:.2f}\n"
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso")
                break
            else:
                print("Digite um valor positivo e inteiro")
    
    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print("Você atingiu o limite de saques")
        else:
            while True:
                saque = float(input("Qual é o valor a ser sacado? "))
                if saque > 500:
                    print("O valor que pode ser sacado é de R$ 500")
                elif saque > saldo:
                    print("Saldo insuficiente")
                elif saque > 0:
                    saldo -= saque
                    extrato += f"Saque realizado de R$ {saque:.2f}\n"
                    numero_saques += 1
                    print(f"Saque de R$ {saque:.2f} realizado com sucesso")
                    break

    elif opcao == "e":
        print("\n------------------Extrato------------------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo em conta: R$ {saldo:.2f}")
        print("---------------------------------------------")
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
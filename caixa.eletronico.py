import os

os.system("cls")


def mostrar_menu():
    print("=== BANCO COFRINHO - CAIXA ===")
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Ver extrato")
    print("0 - Sair")


saldo = 500
extrato = []
opcao = ""


def ver_saldo(saldo):
    print(f"Seu saldo é de R$ {saldo:.2f}")


def realizar_deposito(saldo, extrato):
    deposito = float(input("Digite a quantidade que deseja depositar: "))

    if deposito > 0:
        saldo = saldo + deposito
        extrato.append(f"Depósito: + R$ {deposito:.2f}")
        print(f"Seu depósito foi de R$ {deposito:.2f}")
    else:
        print("Valor inválido!")

    return saldo


def realizar_saque(saldo, extrato):
    saque = float(input("Digite quanto deseja sacar: "))

    if saque > 0 and saque <= saldo:
        saldo = saldo - saque
        extrato.append(f"Saque: - R$ {saque:.2f}")
        print(f"Saque realizado: R$ {saque:.2f}")
    else:
        print("Saldo insuficiente ou valor inválido!")

    return saldo


def ver_extrato(extrato):
    print("=== EXTRATO ===")

    if len(extrato) == 0:
        print("Nenhuma movimentação realizada.")
    else:
        for movimentacao in extrato:
            print(movimentacao)


while opcao != "0":
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            ver_saldo(saldo)

        case "2":
            saldo = realizar_deposito(saldo, extrato)

        case "3":
            saldo = realizar_saque(saldo, extrato)

        case "4":
            ver_extrato(extrato)

        case "0":
            print("Obrigado por utilizar o Banco Cofrinho!")

        case _:
            print("Opção inválida!")

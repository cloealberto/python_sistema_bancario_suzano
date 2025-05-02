# Dados iniciais da conta
LIMITE_SAQUES = 3
limite = 500.00

# Função para exibir o menu principal
def menu():
    print("\n===== CLOE ALBERTO BANK =====")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[0] Sair")
    return input("Escolha a opção desejada: ")

# Função para realizar depósitos
def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: R$ "))
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")
    return saldo, extrato

# Função para realizar saques
def sacar(saldo, extrato, qtde_saques):
    if qtde_saques >= LIMITE_SAQUES:
        print("Limite de saques atingido.")
        return saldo, extrato, qtde_saques

    valor = float(input("Informe o valor do saque: R$ "))
    if valor > limite:
        print(f"Valor acima do limite permitido. O limite é R$ {limite:.2f}.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        qtde_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido para saque.")
    return saldo, extrato, qtde_saques

# Função para exibir o extrato
def exibir_extrato(saldo, extrato):
    print("\n===== CLOE ALBERTO BANK =====")
    if not extrato:
        print("Nenhuma movimentação realizada.")
    else:
        for movimentacao in extrato:
            print(movimentacao)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("===================================")

# Função principal para executar o programa
def main():
    saldo = 0.0
    extrato = []
    qtde_saques = 0

    while True:
        opcao = menu()

        if opcao == "1":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "2":
            saldo, extrato, qtde_saques = sacar(saldo, extrato, qtde_saques)
        elif opcao == "3":
            exibir_extrato(saldo, extrato)
        elif opcao == "0":
            print("Saindo do sistema... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    main()      
    
    
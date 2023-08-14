def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def depositar(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print(f'Saldo da sua conta é de: R${conta["saldo"]}')
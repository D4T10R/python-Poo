class Conta:
    def __init__(self, numero, titular, saldo, limite) -> None: 
        print('Contruindo objeto...')
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite 

    def extrato(self):
        print(f'Saldo da conta {self.titular} é de: R${self.saldo}')

    def deposita(self, valor):
        self.saldo += valor
    
    def saca(self, valor):
        self.saldo -= valor
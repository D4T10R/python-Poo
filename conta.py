class Conta:
    def __init__(self, numero, titular, saldo, limite) -> None: 
        print('Contruindo objeto...')
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite 

class Conta:
    def __init__(self, numero, titular, saldo, limite) -> None: 
        print('Contruindo objeto...')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite 

    def extrato(self):
        print(f'Saldo da conta {self.__titular} é de: R${self.__saldo}')

    def deposita(self, valor):
        self.__saldo += valor
    
    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f'Valor de {valor} é maior do que o saldo e o limite')

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def __pode_sacar(self, valor):
        total_possivel_retirada = self.__saldo + self.limite
        return valor <= total_possivel_retirada

    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite

    @staticmethod
    def codigo_banco():
        return "001"
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor
    
    def ver_saldo(self):
        return self.saldo
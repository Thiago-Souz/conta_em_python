class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("saldo {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __saque_disponivel(self, saque):
     limite_para_saque = self.__saldo + self.__limite
     return saque <= limite_para_saque

    def saca(self, valor):
        if self.__saque_disponivel(valor):
           self.__saldo -= valor
        else:
            print("Saldo indisponível")

    def transfere(self, destino, valor):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite


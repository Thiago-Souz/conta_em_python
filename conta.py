import datetime

class Conta:
    def obter_data_atual(self):
        data_hora_atual = datetime.datetime.now()
        return data_hora_atual

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Extrato da Conta")
        print("Saldo:", round(self.__saldo, 2))
        self.imprime_data_e_hora()


    def depositar(self, valor):
        self.__saldo += valor
        print("Valor depositado:", valor)
        self.imprime_data_e_hora()

    def valor_disponivel(self, valor_saque):
        limite_saque = self.__saldo + self.__limite
        return  valor_saque <= limite_saque

    def sacar(self, valor):
        if self.valor_disponivel(valor):
            self.__saldo -= valor
            self.mensagem_saque(valor)
        else:
            print("Valor indisponível")
            self.imprime_data_e_hora()

    def transfere(self, valor, destino):
        if self.valor_disponivel(valor):
            self.sacar(valor)
            destino.depositar(valor)
            self.mensagem_deposito()
        else:
            print("Valor indisponível para trasnferência.")
            self.imprime_data_e_hora()

    def mensagem_deposito(self, valor, origem, destino):
        print("Transferencia realizada")
        print("Origem", self.__titular)
        print("Origem", destino.__titular)
        self.imprime_data_e_hora()

    def mensagem_saque(self, valor):
        print("Saque realizado.")
        print("valor: R$",valor)
        self.imprime_data_e_hora()

    def imprime_data_e_hora(self):
        data_hora_atual = self.obter_data_atual()
        data_formatada = data_hora_atual.strftime("%d-%m-%Y %H:%M:%S")
        print("Data e hora:", data_formatada)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular.title()

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite += novo_limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':"001", 'CAIXA':"104", 'BRADESCO':"273"}

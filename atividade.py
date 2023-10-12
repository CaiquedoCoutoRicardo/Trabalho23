class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor} efetuado com sucesso.')
        else:
            print('O valor do depósito deve ser maior que zero.')

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f'Saque de R${valor} efetuado com sucesso.')
            else:
                print('Saldo insuficiente para o saque.')
        else:
            print('O valor do saque deve ser maior que zero.')

    def ver_saldo(self):
        print(f'Saldo atual da conta de {self.titular}: R${self.saldo}')


minha_conta = ContaBancaria("João")

minha_conta.depositar(1000)
minha_conta.sacar(500)
minha_conta.depositar(200)
minha_conta.sacar(800)
minha_conta.ver_saldo()

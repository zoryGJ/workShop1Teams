#cuenta bancaria
try:
    class BankAccount:
        def __init__(self):
            self.balance = 0
        
        def depositing(self, amount):
            if amount > 0:
                self.balance += amount
                print('Deposito exitoso')
            else:
                print('El desposito debe ser mayor que cero')
        
        def withdrawing(self, amount):
            if amount > 0:
                if self.balance >= amount:
                    self.balance -= amount
                    print('retiro exitoso')
                else:
                    print('Saldo insuficiente para retirar')

        def checkin(self):
            print(f'saldo actual {self.balance}')

    cuenta = BankAccount()

    cuenta.depositing(200)
    cuenta.checkin()

    cuenta.withdrawing(20)
    cuenta.checkin()
     
except Exception as error:
    print(error)
    print('El programa fallo pero continua')
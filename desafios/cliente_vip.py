class Cliente:
    def __init__(self, nome: str, email: str, saldo: int):
        self.nome = nome
        self.email = email
        self.saldo = saldo
    
    def is_vip(self) -> bool:
        return self.saldo >= 1000

nome = input()
email = input()
saldo = int(input())

cliente = Cliente(nome, email, saldo)

if cliente.is_vip():
    print("VIP")
else:
    print("REGULAR")
from contas import ContaBancaria

minha_conta = ContaBancaria(1000)

minha_conta.depositar(500)

minha_conta.sacar(200)

print("saldo:", minha_conta.ver_saldo())
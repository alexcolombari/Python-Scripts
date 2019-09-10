#!/usr/bin/python
# -*- coding: utf-8 -*-

class ContaPoupanca:
    def __init__(self, nome_titular, numero_conta, saldo):
        self.nome_titular = nome_titular
        self.numero_conta = numero_conta
        self.saldo = saldo

    def ContaPoupanca(self):
        self.nome_titular = ""
        self.numero_conta = ""
        self.saldo = 0.01

    def depositar(self, valor):
        print("Valor depositado: ", valor)
        self.saldo = self.saldo + valor

    def resgatar(self, valor):
        if valor <= self.saldo:
            print("Valor sacado: ", valor)
            self.saldo = self.saldo - valor
        else:
            print("Não foi possível sacar, saldo insuficiente!")
    
    def rendimento(self, porcentagem):
        porcentagem = porcentagem / 100
        self.saldo = self.saldo + (self.saldo * porcentagem)

    def saldo():
        return self.saldo

    def getNumeroConta():
        return self.numero_conta

    def getNomeTitular():
        return self.nome_titular

class ContaCorrente:
    def __init__(self, nome_titular, numero_conta, saldo):
            self.nome_titular = nome_titular
            self.numero_conta = numero_conta
            self.saldo = saldo
            
    def contaCorrente(self):
        self.nome_titular = ""
        self.numero_conta = ""
        self.saldo = 0.01

    def depositar(self, valor):
        print("Valor depositado: ", valor)
        self.saldo = self.saldo + valor

    def resgatar(self, valor):
        if valor <= self.saldo:
            print("Valor sacado: ", valor)
            self.saldo = self.saldo - valor
        else:
            print("Não foi possível sacar, saldo insuficiente!")

    def saldo():
        return self.saldo

    def getNumeroConta():
        return self.numero_conta

    def getNomeTitular():
        return self.nome_titular

class CarteiraClientes:
    poupadores = []
    correntistas = []

    def criarConta(nome, numero_conta, tipo, valor):
        if tipo == 0:
            nova_poupanca = ContaPoupanca(nome, numero_conta, valor)
            poupadores.append(nova_poupanca)
        else:
            nova_conta = ContaCorrente(nome, numero_conta, valor)
            correntistas.append(nova_conta)

        print("{} \n {}".format(correntistas, poupadores))

    def encontrar_conta_corrente(numero_conta):
        conta_encontrada = ContaCorrente()
        for i in range(0, len(correntistas)):
            conta_encontrada = correntistas[i]
            print("\n\n===================================")
            print("Dados encontrados")
            print("===================================")
            print(conta_encontrada.getNomeTitular())
            print(conta_encontrada.getNumeroConta())
            print(conta_encontrada.getSaldo())
            print("===================================\n\n")

        return conta_encontrada

    def encontrar_conta_poupanca(numero_conta):
        conta_p_encontrada = ContaPoupanca()
        for i in range(0, len(poupadores)):
            conta_encontrada = poupadores[i]
            print("\n\n===================================")
            print("Dados encontrados")
            print("===================================")
            print(conta_p_encontrada.getNomeTitular())
            print(conta_p_encontrada.getNumeroConta())
            print(conta_p_encontrada.getSaldo())
            print("===================================\n\n")

        return conta_p_encontrada

    def depositar(numero_conta, tipo, valor):
        if tipo == 1:
            conta_encontrada = encontrar_conta_corrente(numero_conta)
            conta_encontrada.depositar(valor)
        else:
            conta_p_encontrada = encontrar_conta_poupanca(numero_conta)
            conta_p_encontrada.depositar(valor)

    def sacar(numero_conta, tipo, valor):
        if tipo == 1:
            conta_encontrada = encontrar_conta_corrente(numero_conta)
            conta_encontrada.saque(valor)
        else:
            conta_p_encontrada = encontrar_conta_poupanca(numero_conta)
            conta_p_encontrada.resgatar(valor)

class Banco:
    agencia_Araras = CarteiraClientes()
    movimentacao = 0
    numero_conta = "0"
    opcao = 10

    while opcao != 0:
        print("Banco\n============")
        print("1.\t Criar uma conta")
        print("**********************************")
        print("2.\t Deposito em conta corrente")
        print("3.\t Saque em conta corrente")
        print("4.\t Encontrar Conta Corrente")
        print("**********************************")
        print("5.\t Deposito em conta poupanca")
        print("6.\t Saque em conta  poupanca")
        print("7.\t Encontrar conta poupanca")
        print("**********************************")
        print("0.\t Encerrar sistema")

        opcao = input("\nEscolha uma opção: ")

        if opcao == 1:
            nome_cliente = raw_input("Digite o nome do cliente: ")
            tipo = raw_input("Digite 1 para Conta Corrente, 0 para Poupança: ")
            numero_conta = raw_input("Digite o numero da conta: ")
            movimentacao = raw_input("Digite o valor a se depositar: ")
            agencia_Araras.criarConta(nome_cliente, tipo, numero_conta, movimentacao)

        if opcao == 2:
            numero_conta = raw_input("Digite o numero da Conta Corrente: ")
            movimentacao = raw_input("Digite o valor a se depositar: ")
            agencia_Araras.depositar(numero_conta, 1, movimentacao)

        if opcao == 3:
            numero_conta = raw_input("Digite o numero da Conta Corrente: ")
            movimentacao = raw_input("Digite o valor a se sacar: ")
            agencia_Araras.sacar(numero_conta, 1, movimentacao)

        if opcao == 4:
            numero_conta = input("Digite o numero da conta: ")
            agencia_Araras.encontrar_conta_corrente(numero_conta)

        if opcao == 5:
            numero_conta = raw_input("Digite o numero da Conta Poupança: ")
            movimentacao = input("Digite o valor a se depositar: ")
            agencia_Araras.depositar(numero_conta, movimentacao)

        if opcao == 6:
            numero_conta = raw_input("Digite o numero da Conta Poupança: ")
            movimentacao = raw_input("Digite o valor a se sacar: ")
            agencia_Araras.sacar(numero_conta, 0, movimentacao)

        if opcao == 7:
            numero_conta = raw_input("Digite o numero da conta: ")
            agencia_Araras.encontrar_conta_poupanca(numero_conta)

    print("****************************************")
    print("\t Volte sempre!")
    print("****************************************")

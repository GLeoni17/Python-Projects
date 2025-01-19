import os

def opcoes_menu():
    print('0. Sair')
    print('1. Soma')
    print('2. Subtração')
    print('3. Multiplicacao')
    print('4. Divisao')
    print('5. Exponenciação')

def soma(n1, n2):
    print('\n{:.2f} + {:.2f} = {:.2f}\n'.format(n1, n2, n1+n2))

def subtracao(n1, n2):
    print('\n{:.2f} - {:.2f} = {:.2f}\n'.format(n1, n2, n1-n2))

def multiplicacao(n1, n2):
    print('\n{:.2f} * {:.2f} = {:.2f}\n'.format(n1, n2, n1*n2))

def divisao(n1, n2):
    print('\n{:.2f} / {:.2f} = {:.2f}\n'.format(n1, n2, n1/n2))

def exponenciacao(n1, n2):
    print('\n{:.2f} ** {:.2f} = {:.2f}\n'.format(n1, n2, n1**n2))


def menu():
    while True:
        opcoes_menu()
        op = int(input('Insira a operação que deseja realizar: '))
        while op < 0 or op > 5:
            op = int(input('Insira apenas opções entre 0 a 5: '))
        
        os.system('cls' if os.name == 'nt' else 'clear')

        if op == 1: 
            print('>>> + escolhida')
            soma(float(input('Insira o Valor 1: ')), float(input('Insira o Valor 2: ')))

        elif op == 2: 
            print('>>> - escolhida')
            subtracao(float(input('Insira o Valor 1: ')), float(input('Insira o Valor 2: ')))

        elif op == 3: 
            print('>>> * escolhida')
            multiplicacao(float(input('Insira o Valor 1: ')), float(input('Insira o Valor 2: ')))

        elif op == 4: 
            print('>>> / escolhida')
            divisao(float(input('Insira o Valor 1: ')), float(input('Insira o Valor 2: ')))

        elif op == 5: 
            print('>>> ** escolhida')
            exponenciacao(float(input('Insira o Valor 1: ')), float(input('Insira o Valor 2: ')))

        if op == 0 or int(input('Deseja continuar? <0> Sim <1> Nao: ')) == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            return

        os.system('cls' if os.name == 'nt' else 'clear')

menu()
import os
import time

class car:
    def __init__(self, car_id, name, value, is_available):
        self.id = car_id
        self.name = name
        self.value = value
        self.is_available = is_available
    
    def rent(self, available):
        self.is_available = available

    def print_data(self):
        print(f"[{self.id}] \t| [{self.name}] \t| R$ {self.value} por hora.")

    def total_price(self, days):
        print('\nCarro: {}'.format(self.name))
        print('Quantidade de Horas: {}'.format(days))
        print('Preço total: R$ {:.2f}\n'.format(days * self.value))

cars = []

def start():
    # Reads all cars in 'cars.txt' file
    # Saves in 'cars' list
    with open('cars.txt', 'r') as cars_file:
        for line in cars_file:
            fields = line.strip().split(";")
            new_car = car(int(fields[0]), str(fields[1]), float(fields[2]), str(fields[3]))
            cars.append(new_car)

def wait_close(seconds):
    # Only for waiting till message can be read
    for i in range(seconds, 0, -1):
        print('Fechando em {} segundos'.format(i))
        time.sleep(1)

def main_menu():
    # Shows the main menu options
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('0. Sair')
        print('1. Mostrar portfólio')
        print('2. Alugar carro')
        print('3. Devolver carro')
        print('4. Admin\n')

        opt = int(input('>>> '))

        if opt == 0: 
            os.system('cls' if os.name == 'nt' else 'clear')
            return
        
        elif opt == 1:
            show_portfolio('D')
            while int(input('\n0. Sair\n>>> ')) != 0: None

        elif opt == 2: rent_car('alugar')
        elif opt == 3: rent_car('devolver')
        elif opt == 4: admin()

def show_portfolio(mode):
    os.system('cls' if os.name=='nt' else 'clear')

    print('ID \t| Nome \t\t| Preço')

    verify = 0

    for car in cars:
        if car.is_available == mode: 
            car.print_data()
            verify += 1

    if verify == 0: 
        print('')
        if mode == 'D': print('Nao ha carros para alugar!')
        else: print('Nao ha carros para devolver!')

def rent_car(message):
    if message == 'alugar': show_portfolio('D')
    else: show_portfolio('O')

    print('\n0. Sair\nEscolha o carro para {}'.format(message))
    opt = int(input('\n>>> '))

    while opt < 0 or opt > len(cars):
        opt = int(input('Apenas valores entre 0 e {}\n>>> '.format(len(cars))))

    if opt > 0 and message == 'alugar': checkout(opt-1)
    elif opt > 0 and message == 'devolver': return_car(opt-1)

def checkout (opt):
    os.system('cls' if os.name == 'nt' else 'clear')

    days = int(input('Insira quantos dias deseja alugar\n\n>>> '))

    while days < 1:
        days = int(input('Apenas valores maiores que 0\n>>> '))

    cars[opt].total_price(days)

    check = str(input('Você confirma esse valor? <S> <N>\n\n>>> '))

    while check != 'S' and check != 'N':
        check = str(input('<S> <N>\n>>> '))

    if check == 'S': 
        cars[opt].rent('O') 
        os.system('cls' if os.name == 'nt' else 'clear')
        print('{} alugado com sucesso por {} dias!'.format(cars[opt].name, days))
        wait_close(3)

def return_car(opt):
    os.system('cls' if os.name == 'nt' else 'clear')
    check = str(input('Voce tem certeza que deseja devolver o {}? <S> <N>\n>>> '.format(cars[opt].name)))

    while check != 'S' and check != 'N':
        check = str(input('<S> <N>\n>>> '))

    if check == 'S': 
        cars[opt].rent('D') 
        os.system('cls' if os.name == 'nt' else 'clear')
        print('{} devolvido com sucesso!'.format(cars[opt].name))
        wait_close(3)

def admin():
    if str(input('Insira o usuario: ')) != 'admin' or str(input('Insira a senha: ')) != '123456': return

    while True:
        print('0. Sair')
        print('1. Registrar novo carro')
        print('2. Remover carro')
    
        opt = int(input())

        if opt == 0: return
        elif opt == 1: register_car()
        elif opt == 2: remove_car()

        os.system('cls' if os.name == 'nt' else 'clear')

def main():
    start()
    main_menu()

main()
from addition import add
from substraction import sub
from multi import mul
from division import div
from modulo import mod
from potencia import pot
def game():
    score = 0
    
    while True:
        print('======== Menu ========'
              '\n6. Potencia'
              '\n5. Modulo'
              '\n4. Division'
              '\n3. Multiplicacion'
              '\n2. Subtraccion'
              '\n1. Adicion'
              '\n0. Exit')
        option = int(input('\nChoice an option: '))

        if option == 0:
            break

        num_1 = int(input('Enter first number: '))
        num_2 = int(input('Enter second number: '))
        answer = int(input('Enter you answer: '))

        if option == 1:
            result = add(num_1, num_2)
            if result == answer:
                score += 1
                print('Correct!!')
            else:
                print('Incorrect')
        elif option == 2:
            result = sub(num_1, num_2)
            if result == answer:
                score += 1
                print('Correct!!')
            else:
                print('Incorrect')
        elif option == 3:
            result = mul(num_1,num_2)
            if result == answer:
                score += 2
                print('Correct!!')
            else:
                print('Incorrect')
        elif option == 4:
            if num_2!=0:
                result = div(num_1,num_2)
                if result == answer:
                    score += 2
                    print('Correct!!')
                else:
                    print('Incorrect')
            else:
                print("error denominador 0")
        elif option == 5:
            if num_2!=0:
                result = mod(num_1,num_2)
                if result == answer:
                    score += 4
                    print('Correct!!')
                else:
                    print('Incorrect')
            else:
                print("error denominador 0")
        elif option == 6:
            result = pot(num_1, num_2)
            if result == answer:
                score += 4
                print('Correct!!')
            else:
                print('Incorrect')
        
    print(f'======== Game Over ========'
          f'\nYou score is {score}'
          '\nKeep going!')
game()
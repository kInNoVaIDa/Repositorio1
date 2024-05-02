def mod(num_1, num_2):
    if num_2!=0:
        result= num_1 % num_2
        print(f"el residuo de {num_1} / {num_2} es igual a {result}")
        return result
    else: 
        print("error denominador 0")
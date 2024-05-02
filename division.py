def div(num_1, num_2):
    if num_2!=0:
        result= num_1 / num_2
        print(f"la division de {num_1} / {num_2} es igual a {int(result)}")
        return int(result)
    else: 
        print("error denominador 0")
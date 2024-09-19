'''Criar um código (na linguagem de sua preferência) que seja capaz de realizar o MDC de uma quantidade indefinida de números,
 ou seja, o código precisa ser capaz tanto de fazer o MDC de 2 números, 
ou até mesmo de 100, dependendo da quantidade que o usuário requisitar.'''



def mdc():
    numbers = list()
    while True:
        num = int(input('Insira os números para o MDC (0 para encerrar!): '))
        if num != 0:
            numbers.append(num)
            continue
        else:
            break
    numbers.sort(reverse=True)
    while True:
        resposta = numbers[0] % numbers[1]
        if resposta != 0:
            numbers[0] = numbers[1]
            numbers[1] = resposta
            continue
        else:
            if len(numbers) == 2:
                return numbers[1]
            else:
                numbers.pop(0)
                continue

print(mdc())
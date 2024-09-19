'''Criar um código (na linguagem de sua preferência) que seja capaz de realizar o MDC de uma quantidade indefinida de números,
 ou seja, o código precisa ser capaz tanto de fazer o MDC de 2 números, 
ou até mesmo de 100, dependendo da quantidade que o usuário requisitar.'''



def mdc():
    numbers = list() #criação da lista de números
    while True: #loop para o usuário inserir os números de sua preferência.
        num = int(input('Insira os números para o MDC (0 para encerrar!): '))
        if num != 0:
            numbers.append(num)
            continue
        else:
            break
    numbers.sort(reverse=True) #comando para ordenar a lista de números do maior ao menor
    while True: #loop de algoritmo de euclides (dois primeiros algarismos)
        resposta = numbers[0] % numbers[1] #operação de resto de divisão
        if resposta != 0: #condicional de teste "se a resposta for diferente de 0" o divisor é guardado e o resto da operação se torna o divisor
            numbers[0] = numbers[1]
            numbers[1] = resposta
            continue #volta para o começo do loop
        else: #se o resto for = 0.
            if len(numbers) == 2: #teste para ver se há mais números para prosseguir o algoritmo de euclides, se não houver mais, há o retorno da resposta
                return print(f" O MDC dos números inseridos é {numbers[1]}")
            else: #se houver mais números para realizar a operação de euclides.
                numbers.pop(0) #apaga o primeiro elemento da lista e guarda os números que ainda faltam calcular
                continue #volta para o loop da operação de euclides


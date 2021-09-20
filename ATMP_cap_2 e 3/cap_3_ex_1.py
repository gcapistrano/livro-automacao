#"Automatize tarefas maçantes com Python", capítulo 3, exercício 1.
#Modificado para testar funções como argumento de outras.

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

def dobro(n):
    return n * 2
    
#collatz(int(input('Digite um número: ')))  #forma original

while True:
    try:
        print(dobro(collatz(int(input('Digite um número: ')))))
        break
    except:
        print('Digite um número inteiro!')
    
#"Automatizando tarefas maçantes com Python", capítulo 4, exercício 1


def virgulas(lista):
    for i in lista[0:-1]:
       print(i, end=', ')
    print('and ' + lista[-1])
         

lista_exemplo = ['anta', 'boi', 'cavalo', 'doninha', 'elefante']
virgulas(lista_exemplo) #melhorar para retornar como string

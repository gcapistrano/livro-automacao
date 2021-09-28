#"Automatizando tarefas maçantes com Python", capítulo 4, exercício 2 (pág.158
# do pdf)

#Objetivo: criar código para reproduzir, a partir do grid, a figura:
#..OO.OO..
#.OOOOOOO.
#.OOOOOOO.
#..OOOOO..
#...OOO...
#....O....

#Ou seja, transformar as colunas em linhas.




grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]


x = 0
y = 0
for i in grid:
    print(grid[x][y])
    x += 1
    

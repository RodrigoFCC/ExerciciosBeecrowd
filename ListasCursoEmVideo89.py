continuar = 's'
todos = []
while continuar == 's':
    aluno = []
    notas = []
    soma = 0
    media = []
    todos.append(aluno)
    aluno.append(notas)
    aluno.append(media)
    for i in range(1):
        nome = input('Nome: ')
        aluno.append(nome)
        for j in range(2):
            nota = float(input('Nota %d: ' % (j + 1)))
            notas.append(nota)
            soma += nota
        mediaAluno = soma/2
        media.append(mediaAluno)
    continuar = input('Quer continuar? [S/N] ')
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i in range(len(todos)):
    for j in range(len(aluno)):
        if j == 1:
            media = float(todos[i][j][0])
        if j == 2:
            nome = todos[i][j]
    print(f'{i:<4}{nome:<10}{media:>8.1f}')
print('-' *30)
interrompe = 0
while interrompe != 999:
    mostrarNotas = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mostrarNotas != 999:
        print('Notas de %s são %s' % (todos[mostrarNotas][2], todos[mostrarNotas][0]))
        print('-' * 30)
    else:
        interrompe = 999

print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')


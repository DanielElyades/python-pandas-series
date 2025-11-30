# p01: Hello world!
import pandas as pd

# Cria a series de notas

notas = pd.Series([7.6, 5.0, 8.5, 9.5, 6.4])

# Cria a Series alunos

lst_matriculas = ['m02', 'm03', 'm04', 'm05', 'm06']
lst_nomes = ['Bob', 'Dayse', 'Bill', 'Cris', 'Jimi']
alunos = pd.Series(lst_nomes, index=lst_matriculas)

# Imprime as duas Series

print(notas); print('-' * 20)
print(alunos)
print('-' * 20)

# Criar um dicionário

dic_alunos = {'m02' : 'Bob', 'm05' : 'Dayse', 'm06' : 'Cris', 'm07' : 'Jimi'}
alunos = pd.Series(dic_alunos)
print(alunos)
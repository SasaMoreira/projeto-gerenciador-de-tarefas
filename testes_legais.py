'''i = 1

while i < 10:
    print(i)
    i += 1

criancas = ["Sara", "ana", "malu"]

for pessoas in range(len(criancas)):
    print(criancas[pessoas], pessoas)

matriz_numeros = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

for linha in matriz_numeros:
    print(linha)
    for coluna in linha:
        print(coluna)'''

'''def listar_tarefas():
    #Iterando o dicionário
    for tarefa in tarefas:
        print(tarefa)
        #Para cada tarefa, itere os COMPONENTES do DICIONÁRIO
        for chave, valor in tarefa.items():
            # SE a chave do dict for uma str ENTAO imprima.
            if chave == "tarefa":
                print(valor)'''

'''def fazer_big_mac(nome):
    print(f'sanduiche big mac da {nome}')

def fazer_batata(tamanho):
    print(f'batata {tamanho}')   

def preparar_refrigerante(tipo, tamanho):
    print(f'{tipo} {tamanho}')

fazer_big_mac("Sara")
fazer_batata('Grande')
preparar_refrigerante('Coca', 'Média')

def fazer_combro(nome, tamanho_batata,tipo_refri,tamanho_refri):
    fazer_big_mac(nome)
    fazer_batata(tamanho_batata)
    preparar_refrigerante(tipo_refri, tamanho_refri)

fazer_combro("Sara", 'grsnde', 'coca', 'grande')
    

    
def soma(n1, n2):
    return n1 + n2

no = int(input("digite aqui o n1:"))
np = int(input("digite aqui o n2:"))

resul = soma(no, np)
print(resul)

familia = ['ana', 'malu', 'sara', 'alciene','pedro', 'catarina']

familia.index
#print(familia.index("sara"))

try:
    numero = int(('Digite um número'))
    print(numero)

except:
    print('Digite um valor:')'''

# familia = ['ana', 'malu', 'sara', 'alciene','pedro', 'catarina']

# for index, nome in enumerate(familia):
#     print(index, nome)

import os

print(os.name)

print(os.environ.get('username'))
print(os.environ.get('path'))
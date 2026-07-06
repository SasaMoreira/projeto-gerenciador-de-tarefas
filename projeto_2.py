# Importando funcionalidades da biblioteca
import os
import json


# Definindo a nossa função ADCIONAR_TAREFAS; Parâmetros (Convertidos em string)
def adicionar_tarefa(x: str): 
    # Tranferir a tarefa recebida para o dicioário, para receber status
    dict_tarefa = {
        'tarefa': x,
        'esta_feita': False
    }
    # Permitir que novas tarefas sejam adcionadas em formato de dicionário
    tarefas.append(dict_tarefa)

# Definindo a função LISTAR_TAREFAS
def listar_tarefas():
    #Iterando a LISTA para buscar cada elemento dela
    for tarefa in tarefas:
        print(tarefa)
        #Para cada tarefa, itere os COMPONENTES do DICIONÁRIO
        for chave, valor in tarefa.items():
            # SE a chave do dict for uma str ENTAO imprima.
            if chave == "tarefa":
                print(valor)

# Definindo a função para persistir os dados recebidos
def salvar_tarefa(tarefas):
    with open(ARQUIVO_DE_TAREFAS, "w", encoding="utf-8") as file:
        #Salvando a lista de tarefas como JSON formatado
        json.dump(tarefas, file, ensure_ascii=False, indent=4)

# Verificando se há tarefas existentes
def carregar_tarefas():
    if not os.path.exists(ARQUIVO_DE_TAREFAS):
        return []
    # Tentando abrir o arquivo json
    try:
        with open(ARQUIVO_DE_TAREFAS, "r", encoding="utf-8") as file:
            tasks = json.load(file)

            if isinstance(tasks, list):
                return tasks
            else:
                return []
    except:
        print('Algo Correu errado.')

# Crindo lista p/ adcionar tarefa
tarefas=[]

# Iniciando a rotina principal
print("Bem vindo ao gerenciador de tarefas")
while True: 
    tarefa_informada = input("Digite sua tarefa: ")

    #tarefas.append(tarefa)
    adicionar_tarefa(tarefa_informada)
    
    # Contando a quantidade e checando se é maior que 0
    if len(tarefas) > 0:
        print("Tarefas a serem feitas:")
        # Chamando a função para add novoc itens na lista
        listar_tarefas()


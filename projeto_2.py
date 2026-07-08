# Importando funcionalidades da biblioteca
import os
import json

# Atribuindo nome de variável no nosso arquivo json
ARQUIVO_DE_TAREFAS = "tarefas.json"

# Crindo lista p/ adcionar tarefa
tarefas = [] 

# Definindo a função para persistir os dados recebidos
def salvar_tarefa(x):
    with open(ARQUIVO_DE_TAREFAS, "w", encoding="utf-8") as file:
        #Salvando a lista de tarefas como JSON formatado
        json.dump(x, file, ensure_ascii=False, indent=4)

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

# Função de adicinar tarefas (refatorada)
def adicionar_tarefa(): 

    tarefa = input("Digite aqui sua tarefa:")

    # Tranferir a tarefa recebida para o dicioário, para receber status
    dict_tarefa = {
        'tarefa': tarefa,
        'esta_feita': False
    }
    # Permitir que novas tarefas sejam adcionadas em formato de dicionário
    tarefas.append(dict_tarefa)

    # Colocando o input no arquivo json
    salvar_tarefa(tarefas)

    print(f"Tarefa '{tarefa}' adicionada com sucesso! ✅")

# Definindo a função LISTAR_TAREFAS (Alterações)
def listar_tarefas():
    # Listando as tarefas com o enumerate
    print("\n 📎Lista de Tarefas: ")

    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i} - {tarefa['tarefa']}")



# Iniciando a rotina principal
print("Bem vindo ao gerenciador de tarefas")
while True: 
    tarefas = carregar_tarefas()

    print("---------- 📎 Gerenciador de Tarefas 📎 ----------\n")

    print("1 - Adicionar Tarefa")
    print("2 - Listar tarefas existentes")
    print("3 - Finalize uma tarefa (Marcar como concluída)")
    print("4 - Fechar o programa\n")
 
    opcao = int(input("---------- Digite a opção desejada: ---------- "))
    
    if opcao == 1:
        adicionar_tarefa()
    
    elif opcao == 2:
        listar_tarefas()

    #Função ainda não criada
    elif opcao == 3:
        finalizar_tarefa()
    
    elif opcao == 4:
        print("Saindo do programa")
        break
    else:
        print("Opção Inválida. Por favor, digite um número!")

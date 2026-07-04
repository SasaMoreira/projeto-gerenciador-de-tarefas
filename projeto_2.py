# Crindo lista p/ adcionar tarefa
tarefas=[]
# Definindo a nossa função ADCIONAR_TAREFAS; Parâmetros (Convertidos em string)
def adicionar_tarefa(x: str): 
    # Criando um dicionário com diferentes dataTypes;
    # Avaliar os vários status de uma mesma tarefa.
    dict_tarefa = {
        'tarefa': x,
        'esta_feita': False
    }
    # Permitir que novas tarefas sejam adcionadas
    tarefas.append(dict_tarefa)

# Definindo a função LISTAR_TAREFAS
def listar_tarefas():
    #Iterando o dicionário
    for tarefa in tarefas:
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


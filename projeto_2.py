# Crindo lista p/ adcionar tarefa
tarefas=[]
# Definindo a nossa função ADCIONAR_TAREFAS; Parâmetros
#
def adicionar_tarefa(tarefa: str): 
    # Criando um dicionário com diferentes dataTypes;
    # Avaliar os vários status de uma mesma tarefa.
    dict_tarefa = {
        'tarefa': tarefa,
        'esta_feita': False
    }
    # Permitir que novas tarefas 
    tarefas.append(dict_tarefa)

# Definindo a função LISTAR_TAREFAS
def listar_tarefas():
    #Iteração da lista
    for tarefa in tarefas:
        #Iteração dos COMPONENTES do DICIONÁRIO
        for chave, valor in tarefa.items():
            # SE a chave do dict for uma str ENTAO imprima.
            if chave == "tarefa":
                print(valor)

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

'''adicionar_tarefa(tarefa="tarefa 1")    
adicionar_tarefa(tarefa="tarefa 2") 
adicionar_tarefa(tarefa="tarefa 3") 
adicionar_tarefa(tarefa="tarefa 4") 
adicionar_tarefa(tarefa="tarefa 5") 
listar_tarefas()
#print(tarefas)'''
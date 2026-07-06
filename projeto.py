tarefas = []
print("Bem vindo ao gerenciador de tarefas")
while True: 
    tarefa = input("Digite sua tarefa: ")
    
    tarefas.append(tarefa)

    if len(tarefas) > 0:
        print("Tarefas a serem feitas:")
        for afazer in tarefas:
            print(f">{afazer}")
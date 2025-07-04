def add_tasks(tasks, task, data):
    tasks.append({'top': task, 'deadline': data, 'done': False})
    
def show_tasks(tasks):
    if not tasks:
        print("Список задач пуст.")
    else:
        for i, task in enumerate(tasks, 1):
            title = task.get('top', 'Без названия')
            done = "✅" if task.get('done') else "❌"
            deadline = task.get('deadline', 'Без срока')
            print(f"{i}. {title} | {done} | дедлайн: {deadline}")
    
def remove_tasks(tasks, num):
    if 1 <= num <= len(tasks):
        tasks.pop(num - 1)
    else:
        print('Неверный номер задачи')
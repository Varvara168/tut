from storage import *
from todo import *

tasks = load_tasks()
while True:
    print('----------------\n[1] Добавить задачу\n[2] Показать задачи\n[3] Удалить задачу\n[4] Отметить задачу как выполненную\n[5] Очистить все задачи\n[0] Выйти')
    a = input('Введите действие: ')
    print('----------------')
    if a == '1':
        task = input('Введите задачу:')
        data = input('Дедлайн гггг-мм-дд:')
        add_tasks(tasks, task, data)
    elif a == '2':
        show_tasks(tasks)
    elif a == '3':
        show_tasks(tasks)
        num = int(input('Введите номер задачи с 1:'))
        remove_tasks(tasks, num)
    elif a == '4':
        show_tasks(tasks)
        try:
            num = int(input("Введите номер задачи для отметки как выполненной: ")) - 1
            if 0 <= num < len(tasks):
                tasks[num]["done"] = not tasks[num]["done"]
                status = "выполнена" if tasks[num]["done"] else "не выполнена"
                print(f"Задача №{num + 1} теперь {status}.")
            else:
                print("Неверный номер задачи.")
        except ValueError:
            print("Введите корректный номер.")
    elif a == '0':
        break
    elif a == '5':
        m = input("Ты точно хочешь удалить все задачи? (да/нет): ").lower()
        if m == 'да':
            tasks.clear()
            print("Все задачи удалены.")
        else:
            print("Очистка отменена.")
        
    else:
        print('Ввведите номер команлы')
        
    save_tasks(tasks)
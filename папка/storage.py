import json

# Загрузка
def load_tasks(filename='tasks.txt'):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    
# Сохранение
def save_tasks(tasks, filename='tasks.txt'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)
        #url или строка
        #ыорматирование красивое

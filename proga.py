HELP = """
    help - напечатать справку по программе.
    add - добавить задачу в список(название задачи запрашиваем у пользователя).
    show - напечатать задачу на выбранную дату.
    show all - напечатать все добавленные задачи"""

#Задаем пустые списки
tasks = {}


run = True

while run:
    command = input('Введите команду: ')
    if command == 'help':
        print(HELP)
    elif command == 'show':
        whay=input('На какую дату хотите посмотреть задачи?:')
        if whay in tasks:
            print(tasks[whay])
        else:
            print('На данную дату нет задач!')
    elif command == 'show all':
        print(tasks)
    elif command == 'add':
        task = input('Введите название задачи: ')
        days = input('На какой день записать?: ')
        if days in tasks:
            tasks[days].append(task)
        else:
            tasks[days] = [task]
        print(f'Задача {task} добавленна на дату{days}')
    elif command == 'exit':
        run = False
        print('Возвращайся!=)')
    else:
        print('Научись печатать, осел!')
        break


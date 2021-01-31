import dao
from os import system

option = None
Menu = """
        1. Show tasks
        2. Add tasks
        3. Edit tasks title
        4. Mark as done
        5. Modify schedule date
        6. Remove tasks
        0. Exit
        """
while option != 0:
    system("cls")
    print(Menu)
    option = int(input(">>>"))
    if option == 1:
        tasks = dao.readTasks()
        for row in tasks:
            print(f'{row[0]:6d} {row[1]:<30s} {row[2]:5}  {row[3]}   {row[4]}   {row[5]}')
        input("Hit ENTER")

    if option == 2:
        title = input("New task title:  ")
        date_scheduled = input("Schedule date (yyyy-mm-dd) ")
        dao.createTask(title,False,"current_date", date_scheduled)
        print(f'The new task with title "{title}" wes created')
        input("Hit ENTER")

    if option==3:
        id = int(input("Which task id ?:"))
        title = input("Input new title:  ")
        dao.updateTask(id, title)
        print(f'The new title for task ID {id} is "{title}"')
        input("Hit ENTER")

    if option == 4:
        id = int(input("Which task id ?:"))
        dao.updateTask(id, title=None, done=True)
        print(f'The task ID {id} is mark as DONE')
        input("Hit ENTER")

    if option == 5:
        id = int(input("Which task ID ?:"))
        date_scheduled = input("Schedule date (yyyy-mm-dd) ")
        dao.updateTask(id, title=None, done=None, date_scheduled=date_scheduled)
        print(f'The new schedule date for task ID {id} is {date_scheduled}')
        input("Hit ENTER")

    if option == 6:
        id = int(input("Which task id ?:"))
        dao.removeTask(id)
        print(f'Task ID {id} was removed ')
        input("Hit ENTER")
import sqlite3
from datetime import datetime


conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Tasks (
        TaskId INTEGER PRIMARY KEY AUTOINCREMENT,
        TaskName TEXT NOT NULL,
        CreatedOn DATETIME DEFAULT CURRENT_TIMESTAMP,
        Status TEXT DEFAULT 'Not Done'
    )
''')
conn.commit()

def create_task(task_name):
    created_on = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("INSERT INTO Tasks (TaskName, CreatedOn, Status) VALUES (?, ?, ?)", (task_name, created_on, 'Not Done'))
    conn.commit()
    print(f'Task "{task_name}" created successfully.')

def delete_task(task_id):
    cursor.execute("DELETE FROM Tasks WHERE TaskId=?", (task_id,))
    conn.commit()
    print(f'Task with ID {task_id} deleted successfully.')

def show_tasks():
    cursor.execute("SELECT * FROM Tasks")
    rows = cursor.fetchall()
    if not rows:
        print("No tasks found.")
    else:
        print("Task_ID\t\tTask Name\t\tCreated On\t\tStatus")
        for row in rows:
            print(f"{row[0]}\t{row[1]}\t\t{row[2]}\t{row[3]}")

def mark_as_done(task_id):
    cursor.execute("UPDATE Tasks SET Status='Done' WHERE TaskId=?", (task_id,))
    conn.commit()
    print(f'Task with ID {task_id} marked as Done.')


show_tasks()
create = input("Enter new task: ")

create_task(create)
show_tasks()

task_done = int(input("Enter the task ID for which you want to mark as done?: "))
mark_as_done(task_done)
show_tasks()

task_del = int(input("Enter task ID for which you want to delete?: "))
delete_task(task_del)
show_tasks()


conn.close()

import sqlite3

class TaskManager:
    def __init__(self, db_name="../task.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT
        )
        """)

    def add_task(self, task):
        self.cursor.execute("INSERT INTO tasks(task) VALUES(?)", (task,))
        self.conn.commit()

    def view_tasks(self):
        self.cursor.execute("SELECT * FROM tasks")
        return self.cursor.fetchall()
    
    def delete_task(self, task_id):
        self.cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        self.conn.commit()
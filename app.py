import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
# Global tasks List
def init_db():
    with sqlite3.connect('tasks.db') as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT, priority TEXT)')
    conn.close()

def get_tasks():
    with sqlite3.connect('tasks.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM tasks ORDER BY priority DESC')
        tasks = cur.fetchall()
    return tasks

def get_task(task_id):
    with sqlite3.connect('tasks.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
        task = cur.fetchone()
    return task

def add_task(task, priority):
    with sqlite3.connect('tasks.db') as conn:
        conn.execute('INSERT INTO tasks (task, priority) VALUES (?, ?)', (task, priority))
    conn.close()

def update_task(task_id, new_task, new_priority):
    with sqlite3.connect('tasks.db') as conn:
        conn.execute('UPDATE tasks SET task = ?, priority = ? WHERE id= ?', (new_task, new_priority, task_id))
    conn.close()

def delete_task(task_id):
    with sqlite3.connect('tasks.db') as conn:
        conn.execute('DELETE FROM tasks WHERE id= ?', (task_id,))
    conn.close()
# This points to the index.html file in templates directory. Our front-end HTML page
@app.route('/')
def index():
    tasks = get_tasks()
    return render_template('index.html', tasks=tasks)
# This route handles form submission and adds new tasks to the list. 
@app.route('/add', methods=['POST'])
def add ():
    task = request.form.get('task')
    priority = request.form.get('priority')
    if task and priority:
       add_task(task, priority)
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    if request.method == 'POST':
        new_task = request.form.get('task')
        new_priority = request.form.get('priority')
        update_task(task_id, new_task, new_priority)
        return redirect(url_for('index'))
    else:
        task = get_task(task_id)
        return render_template('edit.html', task=task)

# This route handles deleting tasks from the list. 
@app.route('/delete/<int:task_id>', methods=['POST'])
def delete(task_id):
    delete_task(task_id)
    return redirect(url_for('index'))
# This runs the Flask app. 
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
# Global tasks List
tasks = []

# This points to the index.html file in templates directory. Our front-end HTML page
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)
# This route handles form submission and adds new tasks to the list. 
@app.route('/add', methods=['POST'])
def add ():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('index'))
# This route handles deleting tasks from the list. 
@app.route('/delete/<int:task_id>', methods=['POST'])
def delete(task_id):
    if 0<=task_id < len(tasks) :
        tasks.pop(task_id)
    return redirect(url_for('index'))
# This runs the Flask app. 
if __name__ == '__main__':
    app.run(debug=True)
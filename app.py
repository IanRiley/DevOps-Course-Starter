from flask import Flask, render_template, request, redirect, url_for
import session_items as session
app = Flask(__name__)
app.config.from_object('flask_config.Config')

#changed to the template for local host v2.0
#unable to complete the sort by status function 
#new branch created prior to submission

#update from work 2.0
@app.route('/')
def index():
    items = session.get_items()
    return render_template('index.html', todos = items)
    
@app.route('/add', methods=["POST"])
def add_todo():
    item = request.form.get('todo_task')
    session.add_item(item)
    return redirect(url_for('index'))

#delete function 
@app.route('/delete', methods=["POST"])
def delete_todo():
    item = request.form.get('todo_id')
    print(item)
    session.delete_item(item)
    return redirect(url_for('index'))

#update function 
@app.route('/update', methods=["POST"])
def update_todo():
    item = request.form.get('todo_id')
    new_todo_value = request.form.get("title")
    new_status_value = request.form.get("status")
    session.update_item(item, new_todo_value, new_status_value)
    return redirect(url_for('index'))
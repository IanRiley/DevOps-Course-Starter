import os
import requests
import session_items as session
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv

app = Flask(__name__)
app.config.from_object('flask_config.Config')

tr_key=os.getenv("trello_key")
tr_token=os.getenv("trello_token")
tr_board=os.getenv("trello_board")
tr_todo=os.getenv("trello_todo")
tr_inprogress=os.getenv("trello_doing")
tr_done=os.getenv("trello_done")

#tr_key=os.getenv("tr_key")
#tr_token=os.getenv("tr_token")
#tr_board=os.getenv("tr_board")
#tr_todo=os.getenv("tr_todo")
#tr_inprogress=os.getenv("tr_inprogress")
#tr_done=os.getenv("tr_done")


def tr_auth():
    return {'key': tr_key,'token': tr_token}
    
class TrelloTodo:
    def __init__(self, item_id, name, status):
        self.item_id = item_id
        self.name = name
        self.status = status

def set_list(id, list_id):
    tr_parameters = tr_auth()
    tr_parameters['idList'] = list_id
    return requests.put(f"https://api.trello.com/1/cards/{id}", params=tr_parameters)

def set_bye(id):
    tr_parameters = tr_auth()
    return requests.delete(f"https://api.trello.com/1/cards/{id}", params=tr_parameters)

@app.route('/')
def index():

    todo_list_api_response_in_json = requests.get('https://api.trello.com/1/lists/' + tr_todo + '/cards', params=tr_auth()).json()
    
    todo_list_api_response = []
    for iteminjson in todo_list_api_response_in_json:
        todo_list_api_response.append(TrelloTodo(iteminjson['id'],iteminjson['name'], 'todo'))

    doing_list_api_response_in_json = requests.get('https://api.trello.com/1/lists/' + tr_inprogress + '/cards', params=tr_auth()).json()
    doing_list_api_response = []
    for iteminjson in doing_list_api_response_in_json:
        doing_list_api_response.append(TrelloTodo(iteminjson['id'],iteminjson['name'], 'inprogress'))
    
    done_list_api_response_in_json = requests.get('https://api.trello.com/1/lists/' + tr_done + '/cards', params=tr_auth()).json()
    done_list_api_response = []
    for iteminjson in done_list_api_response_in_json:
        done_list_api_response.append(TrelloTodo(iteminjson['id'],iteminjson['name'], 'Done'))
    
    return render_template('new_index.html', list_todo=todo_list_api_response, list_doing=doing_list_api_response_in_json, list_done=done_list_api_response_in_json)



@app.route('/additem', methods=['post'])
def add():
    new_item = request.form.get('new_title')
    tr_parameters = tr_auth() 
    tr_parameters['idList'] = tr_todo
    tr_parameters['name'] = new_item
    requests.post('https://api.trello.com/1/cards', params=tr_parameters)
    return redirect(url_for('index'))


@app.route('/m_todoing/<id>', methods=["GET"])
def set_as_doing(id):

    set_list(id, tr_inprogress)
    return redirect(url_for('index'))

@app.route('/m_tobye/<id>', methods=["GET"])
def say_bye(id):

    set_bye(id)
    return redirect(url_for('index'))

@app.route('/m_todone/<id>', methods=["GET"])
def set_as_done(id):

    set_list(id, tr_done)
    return redirect(url_for('index'))

@app.route('/m_todo/<id>', methods=["GET"])
def set_as_todo(id):

    set_list(id, tr_todo)
    return redirect(url_for('index'))


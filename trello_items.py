import os
import requests
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config.from_object('flask_config.Config')

tr_key=os.getenv("tr_key")
tr_token=os.getenv("tr_token")
tr_board=os.getenv("tr_board")
tr_todo=os.getenv("tr_todo")
tr_inprogress=os.getenv("tr_inprogress")
tr_done=os.getenv("tr_done")


def trello_auth():
    return {'key': tr_key,'token': tr_token}
    

@app_route('/',methods=['GET'])

todo_list_api_response_in_json = requests.get('https://api.trello.com/1/lists/' + tr_todo + '/cards', params=trello_auth()).json()
    
    class_todo_list_api_response = []
    for iteminjson in todo_list_api_response_in_json:
        class_todo_list_api_response.append(Todo(iteminjson['id'],iteminjson['name'], 'To Do'))

    doing_list_api_response_in_json = requests.get('https://api.trello.com/1/lists/' + tr_inprogress + '/cards', params=trello_auth()).json()
    class_doing_list_api_response = []
    for iteminjson in doing_list_api_response_in_json:
        class_doing_list_api_response.append(Todo(iteminjson['id'],iteminjson['name'], 'inprogress'))
    
    done_list_api_response_in_json = requests.get('https://api.trello.com/1/lists/' + tr_done + '/cards', params=trello_auth()).json()
    class_done_list_api_response = []
    for iteminjson in done_list_api_response_in_json:
        class_done_list_api_response.append(Todo(iteminjson['id'],iteminjson['name'], 'Done'))
    
    return render_template('index.html', list_todo=class_todo_list_api_response, list_doing=doing_list_api_response_in_json, list_done=done_list_api_response_in_json)

def create_board(board_name):
    url = "https://api.trello.com/1/boards/"
    querystring = {"name": board_name, "key": key, "token": token}
    response = requests.request("POST", url, params=querystring)
    board_id = response.json()["shortUrl"].split("/")[-1].strip()
    return board_id

def create_list(board_id, list_name):
    url = f"https://api.trello.com/1/boards/{board_id}/lists"
    querystring = {"name": list_name, "key": key, "token": token}
    response = requests.request("POST", url, params=querystring)
    list_id = response.json()["id"]
    return list_id

def create_card(list_id, card_name):
    url = f"https://api.trello.com/1/cards"
    querystring = {"name": card_name, "idList": list_id, "key": key, "token": token}
    response = requests.request("POST", url, params=querystring)
    card_id = response.json()["id"]
    return card_id
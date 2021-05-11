import os
#import requests
#import session_items as session
#from flask import Flask, render_template, request, redirect, url_for

#app = Flask(__name__)
#app.config.from_object('flask_config.Config')

tr_key=os.getenv("trello_key")
tr_token=os.getenv("trello_token")
tr_board=os.getenv("trello_board")
tr_todo=os.getenv("trello_todo")
tr_inprogress=os.getenv("trello_doing")
tr_done=os.getenv("trello_done")

tr_key=os.getenv("tr_key")
tr_token=os.getenv("tr_token")
tr_board=os.getenv("tr_board")
tr_todo=os.getenv("tr_todo")
tr_inprogress=os.getenv("tr_inprogress")
tr_done=os.getenv("tr_done")

from flask import session

_DEFAULT_ITEMS = []

def get_items():
# Fetches all saved items from the session.
    return session.get('items', _DEFAULT_ITEMS)


def get_item(id):
# Fetches the saved ID or None
    items = get_items()
    return next((item for item in items if item['id'] == int(id)), None)


def add_item(title):
#Adds a new item with the title
    items = get_items()

# Get an ID higher than current
    id = items[-1]['id'] + 1 if items else 0

    item = { 'id': id, 'title': title, 'status': "Not Started" }

    items.append(item)
    session['items'] = items

    return item


def save_item(item):
#Update the item with ID, if not valid, skip
    existing_items = get_items()
    updated_items = [item if item['id'] == existing_item['id'] else existing_item for existing_item in existing_items]

    session['items'] = updated_items

    return item


def delete_item(item_id):
#Delete the ID
    existing_items = get_items()
    session['items'] = [ items for items in existing_items if int(items.get('id')) != int(item_id) ]
    
    return item_id
 

def update_status(items, status):
#Update status (if valid)
    if (status.lower().strip() == 'not started'):
        status = NotStarted
    elif (status.lower().strip() == 'in progress'):
        status = InProgress
    elif (status.lower().strip() == 'completed'):
        status = Completed
    else:
        print("Invalid Status: " + status)
        return None


def update_item(item_id, new_todo_value, new_status_value):
#Update text & status
    todo_items = []
    for todo in get_items():
        if int(todo.get('id')) == int(item_id):
            todo['title'] = new_todo_value
            todo['status'] = new_status_value
        todo_items.append(todo)
    session['items'] = todo_items
    return item_id
class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def todo_items(self):
        return list(filter(lambda i: i.status == 'To Do', self._items))

    @property
    def doing_items(self):
        return list(filter(lambda i: i.status == 'Doing', self._items))

    @property
    def done_items(self):
        return list(filter(lambda i: i.status == 'Done', self._items))
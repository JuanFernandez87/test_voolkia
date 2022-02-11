from sqlalchemy import Integer


from sqlalchemy import Integer, String

class Items():
    id_item = Integer
    title = String(30)
    category_id = Integer

def __init__(self, id_item=None, title=None, category_id=None):
    self.id_item = id_item
    self.title = title
    self.category_id = category_id

  
class Field:
    def __init__(self, params):
        self.x = params[0]
        self.y = params[1]
        self.width = params[2]
        self.height = params[3]
        self.value = None

class Grid:
    def __init__(self, params):
        self.dimensions = params
        self.field_indexes = []
        self.field_values = []

class Column:
    def __init__(self, indexes):
        self.field_indexes = indexes
        self.field_values = []

class Row:
    def __init__(self):
        self.field_indexes = None
        self.field_values = []
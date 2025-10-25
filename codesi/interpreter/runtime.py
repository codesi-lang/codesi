

class CodesiFunction:
    def __init__(self, name, params, body, closure):
        self.name = name
        self.params = params
        self.body = body
        self.closure = closure

class CodesiClass:
    def __init__(self, name, parent, methods, constructor):
        self.name = name
        self.parent = parent
        self.methods = methods
        self.constructor = constructor

class CodesiObject:
    def __init__(self, class_def):
        self.class_def = class_def
        self.properties = {}

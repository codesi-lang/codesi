class BreakException(Exception):
    pass

class ContinueException(Exception):
    pass

class ReturnException(Exception):
    def __init__(self, value):
        self.value = value

class CodesiError(Exception):
    def __init__(self, message, suggestion=None):
        self.message = message
        self.suggestion = suggestion
        super().__init__(message)

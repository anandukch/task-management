class TaskException(Exception):
    def __init__(self,code:int, message: str):
        self.status_code = code
        self.message = message
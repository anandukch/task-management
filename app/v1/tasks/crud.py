from app.common import BaseCrud
from app.db import Tasks

class TaskCrud(BaseCrud):
    def __init__(self, db):
        super().__init__(db)

    def get_length(self):
        return self.db.count_documents({})

task_crud = TaskCrud(Tasks)    
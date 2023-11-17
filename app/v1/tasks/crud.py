from app.common import BaseCrud
from app.db import Tasks
class TaskCrud(BaseCrud):
    def __init__(self, db):
        super().__init__(db)

task_crud = TaskCrud(Tasks)    
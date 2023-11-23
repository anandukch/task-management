from pydantic import BaseModel, Field
from bson import ObjectId
from typing import List, Dict


class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=50)
    is_completed: bool = Field(False)

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "title": "Task 1",
                "is_completed": False,
            }
        }


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=50)
    is_completed: bool = Field(False)


class TaskListCreate(BaseModel):
    tasks: list[TaskCreate]


class TaskUpdate(TaskBase):
    pass


class TaskInDB(TaskBase):
    id: str = Field(..., alias="id")

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "id": "1",
                "title": "Task 1",
                "is_completed": False,
            }
        }


class CreateTaskResponse(BaseModel):
    id: str = Field(..., alias="id")


class TaskDelete(BaseModel):
    tasks: List[CreateTaskResponse]


class GetTasksResponse(BaseModel):
    task: List[TaskInDB]

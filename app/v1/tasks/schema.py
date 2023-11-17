from pydantic import BaseModel, Field
from bson import ObjectId

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
    class Config:
        from_attributes = True
        # allow_population_by_field_name = True
        # arbitrary_types_allowed = True
        # json_encoders = {ObjectId: str}

class TaskUpdate(TaskBase):
    pass


class TaskInDB(TaskBase):
    id: str = Field(..., alias="_id")

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "title": "Task 1",
                "is_completed": False,
            }
        }

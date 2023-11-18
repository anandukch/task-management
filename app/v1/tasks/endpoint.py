from fastapi import APIRouter, HTTPException, status, Response
from fastapi.responses import JSONResponse
from app.v1.tasks.crud import task_crud
from app.v1.tasks.schema import TaskCreate, TaskUpdate, TaskInDB
from app.v1.tasks.serializer import taskResponseSerializer, tasksResponseSerializer
from bson import ObjectId

task_router = APIRouter()


@task_router.get("/", status_code=200)
async def get_all_tasks():
    tasks = list(task_crud.get_all())
    return tasksResponseSerializer(tasks)


@task_router.post("/", status_code=201)
async def create_task(task: TaskCreate):
    new_task = {
        "id": task_crud.get_length()+1,
        "title": task.title,
        "is_completed": False,
    }
    task_crud.create(new_task)
    return {"id": task_crud.get_length()}


@task_router.get("/{id}", status_code=200)
async def get_task(id: int):
    task = task_crud.get(id)
    if task:
        return taskResponseSerializer(task)
    else:
        raise HTTPException(status_code=404, detail="There is no task at that id")


@task_router.put("/{id}", status_code=204)
async def update_task(id: int, task: TaskUpdate):
    task = task_crud.update({"id": (id)}, task.model_dump())
    if task:
        return Response(status_code=204)
    else:
        raise HTTPException(status_code=404, detail="There is no task at that id")


@task_router.delete("/{id}", status_code=204)
async def delete_task(id: int):
    task = task_crud.delete(id)
    if task:
        return Response(status_code=204)
    else:
        raise HTTPException(status_code=404, detail="There is no task at that id")

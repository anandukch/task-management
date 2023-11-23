from fastapi import APIRouter, HTTPException, Response
from app.v1.tasks.crud import task_crud
from app.v1.tasks.schema import TaskCreate, TaskUpdate, TaskListCreate,TaskDelete
from app.v1.tasks.serializer import taskResponseSerializer, tasksResponseSerializer
from typing import List, Union

task_router = APIRouter()


@task_router.get("/", status_code=200)
async def get_all_tasks():
    tasks = list(task_crud.get_all())
    return tasksResponseSerializer(tasks)


@task_router.post("/", status_code=201)
async def create_task(task: Union[TaskCreate, TaskListCreate]):
    try:
        if "tasks" in dict(task) and isinstance(task.tasks, list):
            created_ids = []
            index = task_crud.get_length()
            new_tasks = []
            for t in task.tasks:
                new_task = {
                    "id": index + 1,
                    "title": t.title,
                    "is_completed": t.is_completed,
                }
                new_tasks.append(new_task)
                created_ids.append(index + 1)
                index += 1
            task_crud.create_all(new_tasks)
            return {"tasks": [{"id": id} for id in created_ids]}
        else:
            new_task = {
                "id": task_crud.get_length() + 1,
                "title": task.title,
                "is_completed": task.is_completed,
            }
            task_crud.create(new_task)
            return {"id": task_crud.get_length()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


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

@task_router.delete("/", status_code=204)
async def delete_tasks(req: TaskDelete):
    tasks = req.tasks
    for task in tasks:
        task_crud.delete(task['id'])
    
    return Response(status_code=204)
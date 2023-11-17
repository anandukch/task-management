from fastapi import APIRouter, HTTPException, status, Response
from fastapi.responses import JSONResponse
from app.v1.tasks.crud import task_crud
from app.v1.tasks.schema import TaskCreate, TaskUpdate, TaskInDB

task_router = APIRouter()


@task_router.get("/", status_code=200)
async def get_all_tasks():
    tasks: [TaskInDB] = list(task_crud.get_all())
    return Response(status_code=status.HTTP_200_OK, content=tasks)


@task_router.post("/", status_code=201)
async def create_task(task: TaskCreate):
    await task_crud.create(task)
    return Response(status_code=status.HTTP_201_CREATED, content="task created")

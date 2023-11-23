from fastapi import FastAPI, APIRouter, HTTPException, status, Request
from fastapi.responses import JSONResponse
from app.v1.tasks.endpoint import task_router
from fastapi.middleware.cors import CORSMiddleware
from app.exceptions import TaskException

app = FastAPI(title="Recipe API", openapi_url="/openapi.json")

api_router = APIRouter()


@app.exception_handler(TaskException)
async def unicorn_exception_handler(request: Request, exc: TaskException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.message},
    )


@app.on_event("startup")
async def startup_event():
    """
    Startup event
    """
    try:
        print("Connecting to database")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error connecting to database",
        )


@api_router.get("/", status_code=200)
async def root() -> dict:
    """
    Root GET
    """
    return {"message": "Hello World"}


origins = ["http://localhost:5173", "*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


api_router.include_router(task_router, prefix="/v1/tasks", tags=["tasks"])

app.include_router(api_router)


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")

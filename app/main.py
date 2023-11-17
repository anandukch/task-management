from fastapi import FastAPI, APIRouter, HTTPException, Request, Response, status
from app.v1.tasks.endpoint import task_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Recipe API", openapi_url="/openapi.json")

api_router = APIRouter()
# @app.on_event("startup")
# async def startup_event():
#     """
#     Startup event
#     """
#     try:
#         print("Connecting to database")
#     except Exception as e:
#         print(e)


@api_router.get("/", status_code=200)
async def root() -> dict:
    """
    Root GET
    """
    return {"message": "Hello World"}


# @api_router.delete("/delete")
# async def clean_db():
#     """
#     Clean database
#     """
#     try:
#         Books.delete_many({})
#         Authors.delete_many({})
#         BookItems.delete_many({})
#         BookQueue.delete_many({})
#         BookRequests.delete_many({})
#         BookTransactions.delete_many({})
#         Projects.delete_many({})
#         Notifications.delete_many({})
        
#         return {"message": "Database cleaned"}
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST, detail="Error seeding database"
#         )


origins = ["http://localhost:5173", "*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


api_router.include_router(task_router, prefix="/tasks", tags=["tasks"])

app.include_router(api_router)


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")

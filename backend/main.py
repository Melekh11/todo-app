from fastapi import FastAPI
from routes.users import user_router
from routes.todos import todo_router
from routes.tags import tag_router
from database import Base, engine
from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(todo_router)
app.include_router(tag_router)

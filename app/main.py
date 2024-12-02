"""
Миграции. Библиотека alembic
Цель: усвоить новые правила структурирования проекта с использованием FastAPI.
Научиться создавать миграции и подтверждать их при помощи alembic.
"""
from fastapi import FastAPI
from routers import task, user


app = FastAPI()


@app.get('/')
async def root():
    return {"message": "Welcome to Taskmanager"}


app.include_router(task.router)
app.include_router(user.router)

from fastapi import FastAPI

from datetime import date

from models import Idea


app = FastAPI()

db: list[Idea] = []


@app.get("/")
async def hello() -> str:
    return "Hello World from Caleb!"


@app.get("/ideas")
async def get_ideas() -> list[Idea]:
    return db


@app.post("/ideas")
async def create_idea(title: str, content: str) -> None:
    idea = Idea(title=title, content=content, created_at=date.today())
    db.append(idea)

from fastapi import Depends, FastAPI, HTTPException, status

from database import get_db

from models import Idea

from sqlmodel import Session, select

from schemas import CreateIdeasResponse, UpdateIdeaRequest


app = FastAPI()

# db: list[Idea] = []


@app.get("/")
async def hello() -> str:
    return "Hello World from Caleb!"


@app.get("/ideas")
async def get_ideas(db: Session = Depends(get_db)) -> list[Idea]:
    return db.exec(select(Idea)). all()


@app.post("/ideas", status_code=status.HTTP_201_CREATED)
async def create_idea(tittle: str, content: str, db: Session = Depends(get_db)) -> CreateIdeasResponse:
    idea = Idea(tittle=tittle, content=content)
    db.add(idea)
    db.commit()
    return CreateIdeasResponse(id=idea.id)


@app.patch("/ideas/{idea_id}")
async def update_idea(idea_id: int, update_request: UpdateIdeaRequest, db: Session = Depends(get_db)) -> None:
    idea: Idea | None = db.get(Idea, idea_id)

    if idea is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Idea with ID {idea_id} not found")

    if update_request is not None:
        idea.title = update_request.title

    if update_request is not None:
        idea.content = update_request.content

    db.commit()


@app.delete("/ideas/{idea_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_idea(idea_id: int, db: Session = Depends(get_db)) -> None:
    idea: Idea | None = db.get(Idea, idea_id)

    if idea is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Idea with ID {
                            idea_id} not found fool! YOu should have checked if it existed first ")

    db.delete(idea)
    db.commit()

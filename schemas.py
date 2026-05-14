from pydantic import BaseModel


class CreateIdeasResponse(BaseModel):
    id: int


class UpdateIdeaRequest(BaseModel):
    title: str | None
    content: str | None = None

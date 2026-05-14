from sqlmodel import Field, SQLModel


class Idea(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    tittle: str
    content: str

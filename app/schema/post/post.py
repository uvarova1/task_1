from pydantic import BaseModel, UUID4


class PostCreate(BaseModel):
    title: str
    description: str


class PostRead(BaseModel):
    title: str
    description: str

    class Config:
        from_attributes = True

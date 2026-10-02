from pydantic import BaseModel,ConfigDict,Field

class PostBase(BaseModel):
    title: str = Field(min_length=1,max_length=100)
    content: str = Field(min_length=1)
    author : str = Field(min_length=1, max_length=50)


class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    #This is important. It tells Pydantic it can build the model by reading attributes from an arbitrary object (like a SQLAlchemy ORM model instance), not just from dictionaries.
    model_config=ConfigDict(from_attributes=True)

    id: int 
    date_posted : int
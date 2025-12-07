# output in the form of key-value pairs
from typing import TypedDict
from pydantic import BaseModel, Field

## the blog is inherited from the pydantic so it should be in structured format.
class Blog(BaseModel):
    title:str = Field(description="The title of the blog post")
    content:str = Field(description="The main content of the blog post")

class BlogState(TypedDict):
    blog:Blog
    topic:str
    current_language:str


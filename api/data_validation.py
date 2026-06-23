from pydantic import BaseModel,field_validator,Field
from typing import Annotated

class user_data(BaseModel):
    Title: Annotated[str,Field(...,description="Enter movie",examples=["Avatar"])]

    @field_validator("Title")
    @classmethod
    def strip_and_validate(cls,value):
        value = value.strip()
        if not value:
            raise ValueError("Movie name not should be empty")
        return value

    


from pydantic import BaseModel


class Register(BaseModel):
    id: int 
    subject_name: str
    time: float


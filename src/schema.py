from pydantic import BaseModel


class Register(BaseModel):
    subject_name: str
    time: float


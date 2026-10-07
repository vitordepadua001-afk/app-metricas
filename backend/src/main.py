from fastapi import FastAPI

from backend.src.schema import Register

app = FastAPI()
sql = []

@app.get("/register/")
async def view_register():
    return sql

@app.post("/register/")
async def add_register(register: Register):
    register_dict = register.model_dump()
    register_dict["id"] = len(sql) + 1
    sql.append(register_dict)
    return {"message": "Registration created successfully!"}
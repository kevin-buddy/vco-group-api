from typing import Union
from pydantic import BaseModel, EmailStr, Field
from fastapi import FastAPI, HTTPException
from uuid import UUID

from database import MySQL

app = FastAPI()

class Customer(BaseModel):
    id: UUID
    name: str = Field(min_length=1)
    phone: str = Field(max_length=15)
    email: EmailStr = Field(default=None)

customers = []

@app.get("/")
async def read_root():
    tmp = MySQL()
    print(tmp.get_customers())
    return {"Hello": "World"}

# @app.get("/items")
# async def read_items(limit: int, offset: int):
    
#     return {"item_id": item_id, "q": q}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/customer")
async def create_customer(customer: Customer):
    customers.append(customer)
    return customer

@app.put("/customer")
async def update_customer(customer_id: UUID, customer: Customer):
    customers.append(customer)
    return customer

@app.delete("/customer")
async def delete_customer(customer_id: UUID):
    # raise HTTPException(
    #     status_code=404,
    #     detail=f"ID {customer_id} is not found"
    # )
    return customer_id
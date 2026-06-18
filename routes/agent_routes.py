from fastapi import APIRouter
from fastapi import  HTTPException
import uvicorn
from pydantic import BaseModel
from typing import Literal,Optional
from database.agent_db import AgentDB
from database.db_connection import DbConnection
valid_rank=["Junior","Senior","Commander"]
class  AgentIn(BaseModel):
    name:str
    specialty:str
    is_active:bool = True
    completed_mission:int = 0
    failed_mission:int = 0
    agent_rank:str
router=APIRouter()
a=AgentDB()
@router.post("/agents")
def add_new_agent(data:AgentIn):
    new_data=data.model_dump()
    if new_data["agent_rank"] not in valid_rank:
        raise HTTPException(400,"agent_rank must be valid rank")
    return a.create_agent(new_data)

@router.get("/agents")
def get_all_agents():
    return a.get_all_agents()

@router.get("/agents{id}")
def get_agent_by_id(id:int):
    return a.get_agent_by_id(id)

@router.put("/agents/{id}/deactivate")
def deactivat_agent(id):
    return a.deactivate_agent(id)

@router.put("/agents{id}")
def update_agent(id:int,data:dict):
    return a.update_agent(id,data)







from typing import NewType

from fastapi import APIRouter
from fastapi import  HTTPException
import uvicorn
from pydantic import BaseModel
from typing import Literal,Optional
from database.db_connection import DbConnection
from database.mission_db import MissionDB
from database.agent_db import AgentDB
# from agent_routes import logger

router=APIRouter()
mission=MissionDB()
agent=AgentDB()

class MissionIN(BaseModel):
     title:str
     description:str
     location:str
     difficulty:int
     importance:int
     status:str
     assigned_agent_id:int



@router.post("/missions")
def create_mission(data:MissionIN):
    new_data=data.model_dump()
    if 1 > new_data["difficulty"] > 10 :
        raise HTTPException(400,"invalid difficulty")
    elif    1 > new_data["importance"] > 10 :
        raise HTTPException(400,"invalid importance")
    else:
        return mission.create_mission(new_data)

@router.get("/missions")
def gey_all_missions():
    return mission.get_all_missions()

@router.get("/mission{id}")
def get_mission_by_id(id:int):
    mission1=mission.mission_by_id(id)
    print(mission1)
    if not mission:
        raise HTTPException(404,"mission not exist")
    return mission

@router.put("/mission/{id}/assign/{agent_id}")
def assign_mission(id,agent_id):
    agent1=agent.get_agent_by_id(agent_id)
    mission1=mission.mission_by_id(id)
    num_missions=mission.get_open_mission_by_agent(agent_id)
    if not agent1:
        raise HTTPException(404,"agent not exist")
    elif not mission1:
        raise HTTPException(404,"mission not exist")
    elif not agent1["is_active"]:
        raise HTTPException(400,"agent not active")
    elif mission1["status"]=="NEW":
        raise HTTPException(400,"ststus invalid")
    elif len(num_missions)>=3:
        raise HTTPException(400,"to much missions")
    elif mission1["risk_level"]=="CRITICAL" and agent1["agent_rank"]!= "Commander":
        raise HTTPException(400,"the missions need commander")
    else:
        return mission.assign_mission(id,agent_id)
@router.put("/missions/{id}/start")
def start_mission(id:int):
    mission1=mission.mission_by_id(id)
    if not mission1:
        raise HTTPException(404,"mission not found")
    return mission.update_mission_status(id,"ASSIGNED")
@router.put("/missions/{id}/complete")
def end_mission_in_success(id):
    mission1 = mission.mission_by_id(id)
    if not mission1:
        raise HTTPException(404, "mission not found")
    mission.update_mission_status(id,"COMPLETE")
    mission1=mission.mission_by_id(id)
    agent.increment_completed(mission1["assigned_agent_id"])
    return
@router.put("/missions/{id}/fail")
def end_mission_in_fail(id):
    mission1 = mission.mission_by_id(id)
    if not mission1:
        raise HTTPException(404, "mission not found")
    mission.update_mission_status(id,"FAILED")
    mission1=mission.mission_by_id(id)
    agent.increment_failed(mission1["assigned_agent_id"])
    return

@router.put("/missions/{id}/cancel")
def cancelled_mission(id):
    mission1 = mission.mission_by_id(id)
    if not mission1:
        raise HTTPException(404, "mission not found")
    mission.update_mission_status(id,"CANCELLED")
    mission1=mission.mission_by_id(id)
    agent.increment_failed(mission1["assigned_agent_id"])
    return

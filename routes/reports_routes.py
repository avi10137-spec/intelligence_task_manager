from fastapi import APIRouter
from fastapi import  HTTPException
import uvicorn
from pydantic import BaseModel
from typing import Literal,Optional
from database.db_connection import DbConnection
# from agent_routes import logger
from database.mission_db import MissionDB
from database.agent_db import AgentDB
agent=AgentDB()
mission=MissionDB()

router=APIRouter()

@router.get("/reports/summary")
def get_sumary_reports():
    # logger.info("start creat")
    return {"active_agents_count":agent.count_active_agents(),
            "total_missions":mission.count_all_missions(),
            "completed_missions":mission.count_by_status("COMPLETED")
             ,"failed_missions":mission.count_by_status("FAILED"),
                         "critical_missions" :mission.count_critical_missions()}
@router.get("reports/mission-by-status")
def count_mission_by_status():
    # logger.info("start create")

    return {"completed":mission.count_by_status("COMPLETED")
            ,"failed":mission.count_by_status("FAILED"),"cancelled":mission.count_by_status("CANCELLED")}

@router.get("reports/top-agent")
def get_top_agent():
    # logger.info("start create")
    top_agent=mission.get_top_agent()

    return top_agent

print(get_top_agent)

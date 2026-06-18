import uvicorn
from fastapi import FastAPI
from database.db_connection import DbConnection
from routes.agent_routes import router as router_agent
from routes.mission_routes  import router as router_mission

from routes.reports_routes import  router as router_reports
app=FastAPI()
app.include_router(router_mission)
app.include_router(router_agent)
app.include_router(router_reports)












if __name__ =="__main__":
    db = DbConnection()
    db.get_connection()
    db.create_database()
    db.create_table_agents()
    db.create_table_missions()
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
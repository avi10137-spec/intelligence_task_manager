from db_connection import DbConnection
from agent_db import AgentDB
a=AgentDB()
db=DbConnection()
open_missions=["NEW","ASSIGNED","IN_PROGRESS"]
class MissionDB:
    def __init__(self):
        pass
    def calculate_risk_level(self,difficulty,importance):
        risk_level=(difficulty*2)+importance
        if risk_level < 10:
            return f"LOW"
        elif risk_level >= 10 and risk_level <= 17:
            return f"MEDIUM"
        elif risk_level >= 18 and risk_level <= 24:
            return f"HIGH"
        elif risk_level >= 25:
            return f"CRITICAL"

    def create_mission(self,data:dict):
        conn = db.get_connection()
        cur = conn.cursor()
        sql = "INSERT INTO missions (title,description,location,difficulty,importance,status,risk_level,assigned_agent_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (data["title"], data["description"], data["location"], data["difficulty"],data["importance"],data["status"],m.calculate_risk_level(data["difficulty"],data["importance"]),data["assigned_agent_id"])

        cur.execute(sql, values)
        conn.commit()
        new_id = cur.lastrowid
        cur.close()
        conn.close()
        return new_id
    def get_all_missions(self)->list:
        conn = db.get_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM missions")
        all_missions = cur.fetchall()
        return all_missions
    def mission_by_id(self,id:int):
        conn = db.get_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM missions WHERE id = %s", (id,))
        mission = cur.fetchone()
        return mission
    def assign_mission(self,m_id,a_id):
        conn = db.get_connection()
        cur = conn.cursor(dictionary=True)
        sql = "UPDATE missions SET  assigned_agent_id =%s WHERE id = %s"
        values = (a_id, m_id)
        cur.execute(sql, values)
        conn.commit()
        change = cur.rowcount > 0
        cur.close()
        conn.close()
        return change
    def update_mission_status(self,id,status):
        conn = db.get_connection()
        cur = conn.cursor(dictionary=True)
        sql = "UPDATE missions SET  status =%s WHERE id = %s"
        values = (status,id)
        cur.execute(sql, values)
        conn.commit()
        change = cur.rowcount > 0
        cur.close()
        conn.close()
        return change
    def get_open_mission_by_agent(self,id):
        conn = db.get_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT  *  FROM agents WHERE status = ASSIGNED or status = IN_PROGRESS and  assigned_agent_id = %s",(id,))
        total = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return total
    def count_all_missions(self):
        conn = db.get_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT COUNT(*)as total_missions FROM missions")

        total = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return total
    def count_by_status(self,status):
        conn = db.get_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT COUNT(*)as total_missions_of_status FROM missions WHERE status =%s  ",(status,))

        total = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return total
    def count_open_mission(self):
        conn = db.get_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT COUNT(*)as total_missions_of_open FROM missions WHERE status in open_missions ")

        total = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return total
    def count_critical_missions(self):
        conn = db.get_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT COUNT(*) as total_missions_of_critical FROM missions WHERE risk_level = %s ",("CRITICAL",))
        total = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return total
    def get_top_agent(self):
        conn = db.get_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT assigned_agent_id  FROM agent ORDER BY ")
        total = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return total









m=MissionDB()
# print(m.calculate_risk_level(8,9))
# print(m.create_mission({"title":"isuf","description":"look for information","location":"france","difficulty":9,"importance":8,"status":"assigned","assigned_agent_id":7}))
# print(m.get_all_missions())
# print(m.mission_by_id(2))
# print(m.assign_mission(2,8))
# print(m.update_mission_status(1,"IN_PROGRAS"))
# print(m.get_open_mission_by_agent(2))
# print(m.count_all_missions())
# print(m.count_by_status("IN_PROGRAS"))
# print(m.count_open_mission())
# print(m.count_critical_missions())
print(m.get_top_agent())
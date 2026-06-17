from db_connection import DbConnection
db=DbConnection()
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
    def get_all_missions(self):
        conn = db.get_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM missions")
        all_missions = cur.fetchall()
        return all_missions
m=MissionDB()
# print(m.calculate_risk_level(8,9))
# print(m.create_mission({"title":"isuf","description":"look for information","location":"france","difficulty":8,"importance":4,"status":"assigned","assigned_agent_id":4}))
print(m.get_all_missions())
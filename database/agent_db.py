from db_connection import DbConnection
db=DbConnection()
class AgentDB:
    def __init__(self):
        pass
    def create_agent(self,data:dict):
        conn = db.get_connection()
        cur = conn.cursor()
        sql = "INSERT INTO agents (name,speciality,completed_mission,failed_mission,agent_rank) VALUES(%s,%s,%s,%s,%s)"
        values=(data["name"],data["specialty"],data["completed_mission"],data["failed_mission"],data["agent_rank"])
        cur.execute(sql,values)
        conn.commit()
        new_id=cur.lastrowid
        cur.close()
        conn.close()
        return new_id
    def get_all_agents(self)->list:
        conn = db.get_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM agents")
        all_books=cur.fetchall()
        return all_books
    def get_agent_by_id(self,id:int)->dict |None:
        conn = db.get_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM agents WHERE id = %s", (id,))
        agent=cur.fetchone()
        return agent
    def update_agent(self,id:int,data:dict)->bool:
        conn = db.get_connection()
        cur = conn.cursor(dictionary=True)
        lst = [f" {key} = %s " for key in data.keys()]
        stri = ",".join(lst)
        sql = f"UPDATE agents SET {stri} WHERE id = %s "
        valuse = list(data.values()) + [id]
        cur.execute(sql, valuse)
        conn.commit()
        change = cur.rowcount > 0
        cur.close()
        conn.close()
        return change
    def deactivate_agent(self,id:int)->bool:
        conn = db.get_connection()
        cur = conn.cursor(dictionary=True)
        sql= "UPDATE agents SET is_active =%s WHERE id = %s"
        values=(0,id)
        cur.execute(sql,values)
        conn.commit()
        change = cur.rowcount > 0
        cur.close()
        conn.close()
        return change
    def increment_completed(self,id)->bool:
        conn = db.get_connection()
        cur = conn.cursor(dictionary=True)
        sql = "UPDATE agents SET completed_mission = completed_mission+1 WHERE id = %s"
        values = (id,)
        cur.execute(sql, values)
        conn.commit()
        change = cur.rowcount > 0
        cur.close()
        conn.close()
        return change
    def increment_failed(self,id:int)->bool:
        conn = db.get_connection()
        cur = conn.cursor(dictionary=True)
        sql = "UPDATE agents SET failed_mission = failed_mission+1 WHERE id = %s"
        values = (id,)
        cur.execute(sql, values)
        conn.commit()
        change = cur.rowcount > 0
        cur.close()
        conn.close()
        return change
    def get_agent_performance(self,id:int)->dict:
        conn = db.get_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT  completed_mission FROM agents WHERE id = %s ",(id,))
        completed=cur.fetchone()
        cur.execute("SELECT  failed_mission FROM agents WHERE id = %s ",(id,))
        failed=cur.fetchone()
        total=completed["completed_mission"]+failed["failed_mission"]
        return total
    def count_active_agents(self)->int:
        conn = db.get_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT COUNT(*) as total_active FROM agents WHERE is_active = 1")
        total=cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return total







a=AgentDB()
# print(a.create_agent({"name":"nati","specialty":"tevel","completed_mission":1,"failed_mission":1,"agent_rank":"Senior"}))
# print(a.get_all_agents())
# print(a.get_agent_by_id(4))
# a.update_agent(2,{"name":"aron","speciality":"falstin","completed_mission":3,"failed_mission":1,"agent_rank":"Senior"})
# print(a.deactivate_agent(2))
# print(a.increment_completed(2))
# print(a.increment_failed(2))
# a.get_agent_performance(3)
# a.count_active_agents()

























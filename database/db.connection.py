from concurrent.interpreters import create

import mysql.connector
from mysql.connector import Error
class DbConnection:
    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 3306
        self.user = "root"
        self.password = "1234"
        self.database = "intelligence_db"

    def get_connection(self):
        return mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database)

    def create_database(self):
        conn=self.get_connection()
        cur=conn.cursor()
        cur.execute("CREATE DATABASE IF NOT EXISTS intelligence_db")
        print("hallo")
        cur.execute("USE intelligence_db")
        conn.commit()
        print("database intelligence_db created successfully")
        cur.close()
        conn.close()
    def create_table_agents(self):
        # try:
            conn=self.get_connection()
            cur = conn.cursor()
            create_table_agents = """CREATE TABLE IF NOT EXISTS agents
               (id INT PRIMARY KEY AUTO_INCREMENT ,
               name VARCHAR (50) NOT NULL,
               speciality VARCHAR (50) NOT NULL,
               is_active BOOLEAN DEFAULT TRUE,
               completed_mission INT DEFAULT 0,
               failed_mission INT DEFAULT 0,
               agent_rank ENUM ("Junior","Senior","Commander"))"""
            cur.execute(create_table_agents)
            print("table create")
            conn.commit()
            cur.close()
            conn.close()
            return
    def create_table_missions(self):
        conn = self.get_connection()
        cur = conn.cursor()
        create_table_mission= """CREATE TABLE IF NOT EXISTS missions
        ( id INT PRIMARY KEY AUTO_INCREMENT,
         title VARCHAR (50) NOT NULL,
         description TEXT NOT NULL,
         location VARCHAR (50) NOT NULL,
         difficulty INT NOT NULL,
         importance INT NOT NULL,
         status VARCHAR (50) DEFAULT "NEW",
         risk_level VARCHAR (50) NOT NULL,
         assigned_agent_id INT DEFAULT NULL)"""
        cur.execute(create_table_mission)
        print("mission table create")
        conn.commit()
        cur.close()
        conn.close()
        return
db=DbConnection()
db.get_connection()
db.create_database()
db.create_table_agents()
db.create_table_missions()






















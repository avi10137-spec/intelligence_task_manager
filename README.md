# The background of the project

An intelligence unit called shadowNet needs a system
to manage agents and tasks 
The project creates the entire data layer including a connection to SQL 
Creating tables and classes for data management
## The folder structure

intelligence-task-maneger
|-database
      |-db_connection.py
      |-agent_db.py
      |-mission_db.py
|-README.MD
|-requirements.txt
|-.gitignore
## the table structure

## agents table
filed= id-INT,AUTO_INCREMENT,PK
       name-VARCHAR,NOT NULL
       specialty-VARCHAR,NOT NULL
       is_active-BOOLEAN,NOT NULL
       completed mission-INT,NOT NULL
       failed mission-INT,NOT NULL
       agent_rank-ENUM/VARCHAR,NOT NULL
## mission table
filed = id-INT,AUTO_INCREMENT,PK
        title-VARCHAR,NOT NULL
        description-TEXT,NOT NULL
        location-VARCHAR,NOT NULL
        difficulty-INT,NOT NULL
        importance-INT,NOT NULL
        status-VARCHAR,DEAFULT=new,NOT NULL
        risk level-VARCHAR ,NOT NULL
        assigned agent id -INT
## explain on classes

### class db_connection  
Responsible for establishing a connection to the database and creating tables
###  class Agent_DB
Responsible for SQL operations against the agent table.
#### methods
.Create a new agent 
. Return a list of agents
.Return an agent by id or None 
Update agent fields excluding id
Set an agent as inactive by id
Update the number of completed tasks
Update the number of failed tasks
Return agent data by completed,failed,total,success_rate fields
Return the number of active agents
### class MissionDB
Responsible for all SQL operations on the mission table.
#### methods
Create a new task 
Return all tasks
Return a specific task by id
Associate a task to an agent
Update task status
Return a list of open tasks
Count all tasks
Count tasks by status
Count open tasks
Count critical tasks
Return the agent who completed the most tasks

## bisnes role

rank must be junior/senior/commander
difficulty and importance must be between 1-10
risk level is automatically calculated not sent by user
agent with is active= False cannot receive mission
agent cannot hold more than 3 open missions 
if risk level=CRITICAL only aget her rank is commander can receive mission
only mission in status new can be assigned to ASSIGNED status
only mission can be started only mission in ASSIGNED status after IN_PROGRESS
only mission with IN_PROGRESS status can be changed to completed or failed 
only mission in NEW or ASSIGNED status can be canceled

##  run instructions

Clone the file
Upload the docker 
Run the commands
docker run -d --name intelligence-mysql\
-e MYSQL_ROOT_PASSWORD=1234 \
-e MYSQL_DATABASE=intelligence_db \
-p 3306:3306 \
-d mysql:8.0
Check that docker is running
docker ps
Run a connection 
docker exec -it intelligence-mysql mysql -uroot -p1234
docker start 
uvicorn run main.app app --relode
run the server :
http:/127.0.0.1:8000/docs
 
       

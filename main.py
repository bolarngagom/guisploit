from fastapi import FastAPI
from msf_controller import server, shell, launch_session
from msf_controller import client
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:*",
    "http://localhost:3000",
    "http://127.0.0.1:8000",
]

app.add_middleware(CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Job(BaseModel):
    LHOST: str
    LPORT: int

class Session(BaseModel):
    session_id: str
    cmd: str

@app.get("/start_server")
def init_server():
    SERVER_PID = server.up()
    return {'PID': SERVER_PID}




@app.get("/stop_server")
def kill_server():
    res = server.down()
    if res == 0:
        return {'message': 'server is down!'}
    else:
        return {'error': "Something went wrong!"}


@app.get('/server_pid')
def server_pid():
    return {'PID': server.find_pid(55553)}


@app.get('/login')
def login():
    client.login()
    return {'success': 'Client loged in!'}


@app.post('/launch_session')
def launch(job: Job):
    res = launch_session.launch_session(job.LHOST, job.LPORT)
    return res

@app.post('/create_job')
def create_job(job: Job):
    res = client.create_job(job.LHOST, job.LPORT)
    return res

@app.get('/sessions')
def list_sessions():
    res = client.list_sessions()
    return res


@app.post('/exec_cmd')
def sysinfo(session: Session):
    output = shell.exec_cmd(session.session_id, session.cmd)
    return output

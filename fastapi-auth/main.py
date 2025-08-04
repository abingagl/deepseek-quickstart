from fastapi import FastAPI, Depends, HTTPException
from data_store import AGENTS
from models import Agent, User
from auth import get_current_user
from permissions import check_permission

app = FastAPI()


@app.get("/agents/{agent_id}")
def view_agent(agent_id: str, user: User = Depends(get_current_user)):
    if agent_id not in AGENTS:
        raise HTTPException(status_code=404, detail="Agent not found")

    agent = AGENTS[agent_id]

    if not check_permission(user, "view", agent):
        raise HTTPException(status_code=403, detail="Access denied")

    return {"agent_id": agent.id, "name": agent.name, "sensitivity": agent.sensitivity}


@app.post("/agents/{agent_id}/invoke")
def invoke_agent(agent_id: str, user: User = Depends(get_current_user)):
    if agent_id not in AGENTS:
        raise HTTPException(status_code=404, detail="Agent not found")

    agent = AGENTS[agent_id]

    if not check_permission(user, "invoke", agent):
        raise HTTPException(status_code=403, detail="Access denied")

    return {"message": f"Agent {agent.name} invoked by {user.id}"}
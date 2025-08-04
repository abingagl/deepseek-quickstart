from models import User, Agent, Role, Sensitivity

# 模拟用户
USERS = {
    "u1": User(id="u1", role=Role.ADMIN),
    "u2": User(id="u2", role=Role.OWNER),
    "u3": User(id="u3", role=Role.OPERATOR),
    "u4": User(id="u4", role=Role.USER),
}

# 模拟 Agent
AGENTS = {
    "a1": Agent(id="a1", name="HR Assistant", owner_id="u2", sensitivity=Sensitivity.PUBLIC),
    "a2": Agent(id="a2", name="Finance Bot", owner_id="u2", sensitivity=Sensitivity.CONFIDENTIAL),
}
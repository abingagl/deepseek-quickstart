from models import Role, User, Agent

ROLE_PERMISSIONS = {
    Role.ADMIN: {"agent:create", "agent:delete", "agent:update", "agent:view", "agent:invoke"},
    Role.OWNER: {"agent:create", "agent:update", "agent:view", "agent:invoke"},
    Role.OPERATOR: {"agent:invoke", "agent:view"},
    Role.USER: {"agent:view", "agent:invoke"},
}

def check_permission(user: User, action: str, resource: Agent) -> bool:
    perm = f"agent:{action}"
    if perm not in ROLE_PERMISSIONS.get(user.role, set()):
        return False

    if user.role == Role.OWNER and resource.owner_id != user.id:
        return False

    if user.role == Role.USER and resource.sensitivity == "confidential":
        return False

    return True
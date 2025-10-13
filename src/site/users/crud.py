from .schemas import CreateUser


def create_user(user_in: CreateUser):
    user = user_in.model_dump()
    return {"status": "success", "user": user}


def update_user(user_in):
    user = user_in.model_dump()
    return {
        "status": "success",
    }

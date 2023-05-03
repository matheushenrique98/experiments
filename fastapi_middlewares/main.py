import uuid
import os
from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
import sentry_sdk

sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=0.5,
)

class UserModel(BaseModel):
    name: str
    email: str
    
def get_application() -> FastAPI:
    application = FastAPI(title="FastAPI Logging", debug=True)

    return application

app = get_application()

@app.middleware("http")
async def add_request_id(request: Request, call_next):
    request.state.request_id = str(uuid.uuid1())
    
    response = await call_next(request)
    
    response.headers["X-Request-ID"] = request.state.request_id
    
    return response


@app.get("/user/{user_name}/{email}")
async def user(user_name: str, email: str) -> UserModel:
    from time import sleep
    sleep(90)
    return UserModel(name=user_name, email=email)


@app.get("/uuid")
async def root(request: Request):
    return {"request_id": request.state.request_id, "make": request.headers}


@app.get("/sentry-debug")
async def trigger_error():
    try:
        return len(None)   
    except:
        raise HTTPException(status_code=400)

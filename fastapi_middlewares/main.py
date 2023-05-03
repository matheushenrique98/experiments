import uuid
import os
from fastapi import FastAPI, Request
import sentry_sdk
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware


sentry_sdk.init(
    dsn=os.getenv("SENTRY_DNS"),
    # We recommend adjusting this value in production,
    traces_sample_rate=0.5,
)
    
def get_application() -> FastAPI:
    application = FastAPI()
    application.add_middleware(SentryAsgiMiddleware)
    return application


app = get_application()

@app.middleware("http")
async def add_request_id(request: Request, call_next):
    len(None)
    request.state.request_id = str(uuid.uuid1())
    
    response = await call_next(request)
    
    response.headers["X-Request-ID"] = request.state.request_id
    
    return response


@app.get("/uuid")
async def root(request: Request):
    return {"request_id": request.state.request_id, "make": request.headers}


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.route_log import app_router

app = FastAPI()


app.include_router(app_router, prefix="/api", tags=["teste"])




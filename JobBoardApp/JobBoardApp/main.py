from fastapi import FastAPI
from .job_routes import router as jobsroutes
from auth.auth_routes import router as authroutes

app = FastAPI(title="Simple Job Board API")

app.include_router(jobsroutes)

app.include_router(authroutes)
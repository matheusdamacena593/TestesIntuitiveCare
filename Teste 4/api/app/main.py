from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import operadoras

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(operadoras.router)

@app.get("/")
async def root():
    return {"message": "API Online!"}
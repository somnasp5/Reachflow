from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.csv_routes import router as csv_router
from app.routes.placement_routes import router
from app.routes.email_routes import  router as email_router 
app = FastAPI()

# CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
app.include_router(csv_router)
app.include_router(email_router)

@app.get("/")
def home():
    return {"message": "PlacementGPT Backend Running"}
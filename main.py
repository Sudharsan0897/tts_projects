from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Add if needed for frontend
import router
from database import engine, Base
# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="tts project")

# CORS if frontend (optional)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Include your routers (add auth if separate)
app.include_router(router.router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "tts Projects API Live 🚀"}

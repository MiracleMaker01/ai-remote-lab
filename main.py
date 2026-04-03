from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "success", "message": "Welcome to Day 2 AI Lab API"}

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "active"}
from fastapi import FastAPI

app = FastAPI(title="AI Remote Dev Lab - Day 2")

@app.get("/")
async def read_root():
    return {"status": "success", "message": "Welcome to AI Remote Dev Lab - Day 2"}

@app.get("/health")
async def health_check():
    return {"cpu_status": "OK", "memory_usage":"Normal", "disk_space":"Healthy", "status": "ok", "service": "active"}

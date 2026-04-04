import sqlite3
from fastapi import FastAPI, Query

app = FastAPI(title="AI Remote Dev Lab - Day 3")

# 初始化資料庫 : 建立一個紀錄當天心情或任務的表
def init_db():
    conn = sqlite3.connect("data/lab.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, content TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)")
    conn.commit()
    conn.close()

init_db()

@app.get("/")
def read_root():
    return {"status": "success", "message": "Welcome to AI Remote Dev Lab - Day 3"}

@app.post("/logs")  # 確保路徑與 GET 一致
def add_log(content: str = Query(...)): #明確要求這是一個必要的查詢參數
    conn = sqlite3.connect("data/lab.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO logs (content) VALUES (?)", (content,))
    conn.commit()
    conn.close()
    return {"status": "success", "message": "Log saved successfully"}

@app.get("/logs")
def get_logs():
    conn = sqlite3.connect("data/lab.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM logs")
    rows = cursor.fetchall()
    conn.close()
    return {"status": "success", "data": rows}

# AI Remote Dev Lab - Progress Report

## 📌 專案簡介

本計畫為期 30 天，目標建立：

* 標準化開發環境
* API 服務化能力
* 容器化部署流程

---

## 📅 Day 1：環境建置

### ✔ 完成項目

* 建立 Python 開發環境
* 完成 Docker 容器化
* 建立 Git 版本控制

### 🛠 使用技術

* Python 3.11
* Docker
* Git

---

## 📅 Day 2：API 服務化

### ✔ 完成項目

* 將應用升級為 Web API
* 建立 FastAPI 架構
* 完成 Port Mapping 對外服務

### 🛠 使用技術

* FastAPI
* Uvicorn

---

## 📊 當前成果

* 已具備容器化應用部署能力
* 可透過 API 對外提供服務

---

## 🚧 下一步規劃

* API 文件化（Swagger）
* Docker Compose 多服務整合
* 部署到雲端環境

---

## Day 3 - 資料持久化（SQLite + Docker Volume）

### 🧠 學習目標

* 理解容器無狀態（stateless）問題
* 實作資料持久化（persistent storage）
* 建立 API + DB 整合流程

---

## 🔧 SOP（實作流程）

### Step 1：建立資料庫功能

使用 SQLite 建立 logs table，並在啟動時初始化

### Step 2：設定 Docker 資料目錄

```dockerfile
RUN mkdir -p /app/data
```

### Step 3：重新建置（避免快取）

```bash
docker build --no-cache -t ai-lab-v3 .
```

### Step 4：掛載 Volume

```bash
docker run -p 8080:8000 -v "${PWD}/data:/app/data" ai-lab-v3
```

### Step 5：驗證

* 新增資料
* 關閉容器
* 重啟後確認資料存在

---

## 🧩 核心程式碼

### main.py

```python
import sqlite3
from fastapi import FastAPI, Query

app = FastAPI(title="AI Remote Dev Lab - Day 3")

def init_db():
    conn = sqlite3.connect("data/lab.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY,
            content TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.post("/logs")
def add_log(content: str = Query(...)):
    conn = sqlite3.connect("data/lab.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO logs (content) VALUES (?)", (content,))
    conn.commit()
    conn.close()
    return {"status": "success"}

@app.get("/logs")
def get_logs():
    conn = sqlite3.connect("data/lab.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM logs")
    rows = cursor.fetchall()
    conn.close()
    return {"data": rows}
```

---

## 🐳 Dockerfile

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p /app/data
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## ⚠️ 問題與排錯

* Docker cache 問題 → `--no-cache`
* Uvicorn module 錯誤 → `main:app`
* Volume 空資料 → 檢查 `-v` 路徑

---

## 📒 技術筆記

* SQLite 適合輕量應用
* Docker Volume 本質是 bind mount
* Container ≠ Storage

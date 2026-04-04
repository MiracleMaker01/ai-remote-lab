# 🚀 AI Remote Dev Lab

> 30 Days to Become a Remote AI Engineer

---

## 📚 Overview

This project documents a 30-day journey to:

* Build a standardized dev environment
* Learn containerization (Docker)
* Develop API services (FastAPI)

---

## 🗓 Progress

### Day 1 - Environment Setup

* Python 3.11 setup
* Docker containerization
* Git version control

```bash
docker build -t ai-lab-v1 .
docker run ai-lab-v1
```

---

### Day 2 - FastAPI Service

* Convert script into Web API
* Add port mapping

```bash
docker build -t ai-lab-v2 .
docker run -p 8080:8000 ai-lab-v2
```

---

## 🛠 Tech Stack

* Python
* Docker
* FastAPI
* Uvicorn

---

## 📈 Roadmap

* [ ] API documentation
* [ ] Docker Compose
* [ ] Cloud deployment

---

## ⭐ Highlights

* Clean architecture
* Container-ready
* API-first design

---

# AI Remote Dev Lab - Progress Report

## 📅 Day 3：資料持久化實作

### 🎯 目標

解決容器無法保存資料問題，建立可持續儲存機制

---

## ✔ 完成項目

* 建立 SQLite 資料庫
* API 整合資料存取
* Docker Volume 掛載
* 成功驗證資料持久化

---

## 🛠 技術應用

* SQLite（輕量資料庫）
* FastAPI（API 層）
* Docker Volume（資料持久化）

---

## 📊 成果

* API 可寫入與讀取資料
* 容器重啟後資料不遺失
* 建立基本資料層架構

---

## 🚧 問題與解法

| 問題        | 解法              |
| --------- | --------------- |
| Docker 快取 | 使用 --no-cache   |
| API 無法存取  | 檢查 port mapping |
| 資料未保存     | 正確設定 volume     |

---

## 📈 下一步

* ORM（SQLAlchemy）
* 多資料庫支援
* Docker Compose


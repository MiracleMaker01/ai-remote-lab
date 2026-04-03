# AI Remote Dev Lab

## 📌 專案目標

30 天遠端工程師訓練計畫
建立標準化開發環境、容器化與 API 架構能力

---

## Day 1 - 環境建置

### 🧠 學習重點

* Docker 基本概念（Image / Container）
* Python 執行環境隔離

### 🛠 技術棧

* Python 3.11
* Docker
* Git

### 🚀 執行方式

```bash
docker build -t ai-lab-v1 .
docker run ai-lab-v1
```

### ⚠️ 問題與解法

* 問題：Container 執行後立即結束
* 原因：沒有長時間執行程序
* 解法：加入 main loop 或 server

### 📒 筆記

* Docker Image 是 immutable
* Container 是 runtime instance

---

## Day 2 - API 服務化

### 🧠 學習重點

* FastAPI 基本架構
* Port Mapping

### 🛠 技術棧（新增）

* FastAPI
* Uvicorn

### 🚀 執行方式

```bash
docker build -t ai-lab-v2 .
docker run -p 8080:8000 ai-lab-v2
```

### ⚠️ 問題與解法

* 問題：外部無法存取 API
* 原因：未做 port mapping
* 解法：使用 `-p`

### 📒 筆記

* FastAPI 預設跑在 8000
* Uvicorn 是 ASGI server

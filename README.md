# AI Remote Dev Lab - Day 1

## 📌 專案簡介
本專案為「30天遠端工程師衝刺計畫」的基礎建設，旨在建立標準化的開發環境與版本控制規範。

## 🛠️ 技術棧
- **Language:** Python 3.11
- **Container:** Docker
- **VCS:** Git

## 🚀 如何運行
確保你的電腦已安裝 Docker，執行以下指令：
```bash
docker build -t ai-lab-v1 .
docker run ai-lab-v1

---

# AI Remote Dev Lab - Day 2

## 📌 專案進度：FastAPI 服務化
今天將靜態腳本升級為非同步 Web API，並實作端口映射 (Port Mapping)。

## 🛠️ 新增技術棧
- **Framework:** FastAPI
- **Server:** Uvicorn
- **Tools:** Swagger UI (自動文件)

## 🚀 運行指令
```bash
docker build -t ai-lab-v2 .
docker run -p 8080:8000 ai-lab-v2
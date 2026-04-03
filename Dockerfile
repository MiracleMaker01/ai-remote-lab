FROM python:3.11-slim
WORKDIR /app
COPY . /app
# 安裝依賴套件
RUN pip install --no-cache-dir -r requirements.txt
# 開啟 8000 連接埠
EXPOSE 8000
# 啟動 Uvicorn 伺服器
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

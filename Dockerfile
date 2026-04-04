FROM python:3.11-slim
WORKDIR /app
COPY . /app

# 安裝依賴套件
RUN pip install --no-cache-dir -r requirements.txt

# 建立存放資料的資料夾
RUN mkdir -p /app/data

# 開啟 8000 連接埠
EXPOSE 8000

# 加入這一行，確保 Python 會在當前目錄尋找模組
ENV PYTHONPATH=/app

# 啟動 Uvicorn 伺服器
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

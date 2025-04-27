FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
COPY app.py .
COPY xgboost-model.pkl .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8001

CMD ["python", "app.py"]
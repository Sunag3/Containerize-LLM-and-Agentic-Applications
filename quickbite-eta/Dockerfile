FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 1. Copy ONLY requirements.txt first
COPY requirements.txt .

# 2. Install dependencies (Docker will cache this step if requirements.txt hasn't changed!)
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copy the rest of your application code and model files afterward
COPY . /app/

# 4. Train the model INSIDE the image (baked in at build time)
RUN python train.py

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && apt-get install -y gcc python3-dev && \
    pip install --no-cache-dir uv && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

COPY ./pyproject.toml ./uv.lock ./

RUN uv pip install . --system --no-cache-dir

COPY ./. .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
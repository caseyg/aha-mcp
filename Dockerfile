FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml requirements.txt ./
RUN pip install --no-cache-dir .
COPY . .
EXPOSE 8000
CMD ["python", "aha_mcp.py"]

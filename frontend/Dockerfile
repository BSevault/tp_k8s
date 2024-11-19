FROM python:3.9-slim
WORKDIR /app
COPY frontend.py static templates /app/
RUN pip install flask requests
CMD ["python", "frontend.py"]
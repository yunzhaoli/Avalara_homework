FROM python:3.10

WORKDIR /api

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY api.py .
COPY test_api.py .
COPY README.md .

EXPOSE 5000

CMD ["python", "api.py"]

FROM python:3.13-bookworm

ADD main.py .

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["python", "./main.py"]


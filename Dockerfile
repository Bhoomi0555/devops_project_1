FROM python:3.12-slim

WORKDIR /app

COPY requirements files

RUN pip install -r requirements.txt

copy . 

EXPOSE 5000


CMD ["python" , "app.py"]

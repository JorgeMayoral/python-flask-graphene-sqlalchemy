FROM python:latest

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

RUN python3 seed.py

ENV FLASK_APP=App.py

CMD ["python3", "app.py"]
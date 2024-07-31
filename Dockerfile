FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY weather.py .
COPY weather.html .

EXPOSE 5000

CMD ["python", "weather.py"]
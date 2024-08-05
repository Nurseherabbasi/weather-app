FROM python:3.10
COPY . app
WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

# COPY weather.py .
# COPY weather.html .
# COPY styles.css .

EXPOSE 5000

CMD ["python", "weather.py"]
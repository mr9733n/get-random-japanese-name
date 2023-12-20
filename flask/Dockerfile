FROM python:alpine
WORKDIR /app

COPY japanese_name_generator.py .
COPY requirements.txt .
COPY app.py .
COPY ./templates/index.html ./templates/index.html
COPY ./static/styles.css ./static/styles.css

RUN pip install -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0", "--port=37011"]

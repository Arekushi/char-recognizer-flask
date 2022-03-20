### 2. BUILD ###
FROM python:3.9-slim
WORKDIR /app
COPY ["requirements.txt", "./"]

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000

### 2. RUN ###
ENTRYPOINT ["python"]
CMD ["wsgi.py"]

# docker build -t char-recognizer-flask:latest .
# docker run -p 5000:5000 char-recognizer-flask:latest

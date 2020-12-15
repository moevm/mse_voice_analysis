FROM python:3.8
RUN mkdir app
COPY requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install -r requirements.txt
RUN apt-get update -y
RUN apt-get install gcc -y
RUN apt-get install libsndfile-dev -y
RUN apt-get install ffmpeg -y
COPY . .

#CMD ["python", "src/main.py", "-h"]

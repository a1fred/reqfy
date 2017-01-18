FROM python:3.5

ENV PYTHONUNBUFFERED 1

EXPOSE 8000

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN pip install -Ur requirements.txt; chmod a+x /app/reqfy.py

CMD ["python", "/app/reqfy.py"]

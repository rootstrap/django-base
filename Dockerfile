FROM python:3
ENV PYTHONUNBUFFERED 1
ENV ENV_ROLE docker
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

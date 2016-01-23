FROM python:3.4-onbuild
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN apt-get install -y netcat
RUN apt-get install -y postgresql postgresql-contrib
RUN mkdir -p /karolin/static
RUN mkdir /karolin/media
WORKDIR /karolin
ADD requirements.txt /karolin
RUN pip install -r requirements.txt
ADD . /karolin
RUN chmod +x /karolin/entrypoint.sh

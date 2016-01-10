FROM python:3.4-onbuild
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN apt-get install -y netcat
RUN mkdir -p /karolin/static
WORKDIR /karolin
ADD requirements.txt /karolin
RUN pip install -r requirements.txt
ADD . /karolin
RUN chmod +x /karolin/entrypoint.sh

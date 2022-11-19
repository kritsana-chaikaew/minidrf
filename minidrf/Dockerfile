FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY minidrf/ /app/

RUN pip3 install -r /app/requirements.txt

EXPOSE 8000

CMD ["python", "/app/manage.py", "runserver" , "0.0.0.0:8000"]
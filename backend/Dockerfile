FROM python:3.10.8-slim

ENV PyTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_APP=src/app.py

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /backend
WORKDIR /backend
RUN chmod +x entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]
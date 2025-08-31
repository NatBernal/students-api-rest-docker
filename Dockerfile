FROM python:3.9-alpine

WORKDIR /app

COPY app.py .
RUN mkdir -p data

RUN pip install flask

EXPOSE 4000

CMD ["python", "app.py"]

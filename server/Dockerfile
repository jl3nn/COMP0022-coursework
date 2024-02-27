FROM python:3.12

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5555

CMD ["gunicorn", "server:app", "-w", "24", "-b", "0.0.0.0:5555"]

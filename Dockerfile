FROM python:3.8-slim-buster

RUN apt upatae -y && apt install awscli -y
WORKDIR /app

COPy . /app
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN pip install .

CMD ["Predictive-Sales-Analytics-Ecommerce"]

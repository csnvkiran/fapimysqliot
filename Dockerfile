FROM python:3.8-slim

COPY ./requirements.txt /iotapp/requirements.txt
RUN pip install -r /iotapp/requirements.txt

EXPOSE 8080

COPY ./app /iotapp
COPY ./main.py /iotapp/main.py

HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=2 CMD curl --fail http://localhost:8080/ping || exit1

CMD ["uvicorn", "iotapp.main:app", "--host" , "0.0.0.0", "--port", "8080"]
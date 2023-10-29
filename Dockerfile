FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN  pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
COPY ./main.py /code/main.py

HEALTHCHECK --interval=30s --timeout=3s --start-period=10s --retries=2 CMD curl --fail http://localhost:80/ping || exit1

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

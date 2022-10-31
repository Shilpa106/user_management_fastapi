FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

FROM python:3.8.9
COPY ./main.py .
COPY ./database.py .
COPY ./models.py .
COPY ./schemas.py .
COPY routerapi .
COPY awscognito .
COPY ./backend .
COPY . .

COPY ./requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

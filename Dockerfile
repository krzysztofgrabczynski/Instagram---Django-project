FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8000

RUN mkdir -p /code/data

ENV DB_PATH /code/data/db.sqlite3
RUN sed -i 's/\/code\/db.sqlite3/$DB_PATH/' /code/Instagram/settings.py

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
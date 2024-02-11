FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH "/root/.local/bin:$PATH"

COPY poetry.lock pyproject.toml /code/
COPY README.md /code/

RUN poetry install --no-root

COPY . /code/

RUN poetry install

EXPOSE 8000

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT [ "/docker-entrypoint.sh" ]

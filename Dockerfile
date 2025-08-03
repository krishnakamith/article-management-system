FROM python:3.13.5
ENV PYTHONUNBUFFERED=1

RUN mkdir /code

WORKDIR /code

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && poetry install --no-root 

COPY . .

EXPOSE 8000

ENTRYPOINT [ "poetry", "run", "/code/start-django.sh" ]
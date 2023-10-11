FROM python:3.11-slim AS base
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get autoremove -y

FROM base AS install
WORKDIR /app

# allow controlling the poetry installation of dependencies via external args
ARG INSTALL_ARGS="--no-root --only main"
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
COPY . /app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port",  "8000"]

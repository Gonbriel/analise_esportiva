FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    r-base \
    libpq-dev \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

RUN R -e "install.packages(c('tidyverse','jsonlite','DBI','RPostgres','shiny','flexdashboard','DT','plotly'), repos='https://cloud.r-project.org')"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]

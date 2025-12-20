FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# ─────────────────────────────────────────────
# Dependências de sistema
# ─────────────────────────────────────────────
RUN apt-get update && apt-get install -y \
    r-base \
    pandoc \
    libpq-dev \
    gcc \
    g++ \
    make \
    libcurl4-openssl-dev \
    libssl-dev \
    libxml2-dev \
    && rm -rf /var/lib/apt/lists/*

# ─────────────────────────────────────────────
# Pacotes R (inclui rmarkdown!)
# ─────────────────────────────────────────────
RUN R -e "install.packages( \
    c('rmarkdown','tidyverse','jsonlite','DBI','RPostgres','flexdashboard','DT','plotly'), \
    repos='https://cloud.r-project.org' \
)"

# ─────────────────────────────────────────────
# App Python
# ─────────────────────────────────────────────
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]

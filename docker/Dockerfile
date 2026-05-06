FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    gdal-bin \
    libgdal-dev \
    binutils \
    libproj-dev \
    gcc \
    g++ \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


CMD ["gunicorn", "geotech.wsgi:application", "--bind", "0.0.0.0:8000"]
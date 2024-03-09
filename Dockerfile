#
# Copyright (C) 2024 BurnedPy.
#
# BurnedPy is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

FROM python:3.11-alpine3.18

ENV SPATIALITE_LIBRARY_PATH=mod_spatialite

# Configuring spatialite
COPY --from=geocodio/alpine-spatialite /usr/lib/ /usr/lib
COPY --from=geocodio/alpine-spatialite /usr/bin/ /usr/bin

# Working directory
WORKDIR /app

# Base dependencies
RUN apk --no-cache --update-cache add \
    && apk add --update --no-cache \
        git \
        python3 \
        python3-dev \
        gdal \
        gdal-dev \
        proj \
        proj-dev \
        proj-util \
        geos \
        geos-dev \
        make \
        g++ \
        gcc \
        gfortran \
        py-pip \
        build-base \
        wget \
        freetype-dev \
        libpng-dev \
        openblas-dev \
    && ln -s /usr/include/locale.h /usr/include/xlocale.h \
    && python3 -m ensurepip \
    && pip install poetry \
    && poetry config virtualenvs.create false

# Copy application
COPY . .

# Application dependencies
RUN pip install --no-cache-dir .

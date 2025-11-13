FROM postgres:16

ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=admin
ENV POSTGRES_DB=basicDB

# Install PostGIS
RUN apt-get update \
    && apt-cache showpkg postgresql-$PG_MAJOR-postgis-3 \
    && apt-get install -y --no-install-recommends \
           postgresql-$PG_MAJOR-postgis-3 \
           postgresql-$PG_MAJOR-postgis-3-scripts \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 5432

# VOLUME ["/var/lib/postgresql/data"]


COPY druga/druga_data/simplified_data/*.csv /csvs/
COPY druga/scripts/ /scripts/
COPY druga/scripts/00_main.sql /docker-entrypoint-initdb.d/

# automatic excecution at startup
# COPY scripts/00_main.sql /docker-entrypoint-initdb.d/
# COPY druga/druga_data/scripts/00_main.sql /docker-entrypoint-initdb.d/
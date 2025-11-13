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

VOLUME ["/var/lib/postgresql/data"]
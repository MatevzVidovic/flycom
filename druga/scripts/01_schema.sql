CREATE EXTENSION IF NOT EXISTS postgis;

CREATE TABLE IF NOT EXISTS si_gurs_kn_slo_hisne_st (
    eid_hisna_stevilka BIGINT PRIMARY KEY,
    gurs_potencial INTEGER
);

CREATE TABLE IF NOT EXISTS si_gurs_kn_ds (
    eid_hisna_stevilka BIGINT,
    vrsta_dejanske_rabe_del_st_id INTEGER
);

CREATE TABLE IF NOT EXISTS points (
    id TEXT PRIMARY KEY,
    old_id INTEGER,
    napacen_hmid TEXT,
    potencial_stat INTEGER,
    pravi_potencial FLOAT,
    zacasni_potencial FLOAT,
    eid_hisna_stevilka_key BIGINT,
    point_type_id TEXT
);

CREATE TABLE IF NOT EXISTS omarice_api (
    idjasek INTEGER PRIMARY KEY,
    idstatusomara INTEGER
);
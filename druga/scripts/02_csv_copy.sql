
COPY si_gurs_kn_slo_hisne_st 
FROM '/csvs/si_gurs_kn_slo_hisne_st.csv' 
DELIMITER ',' 
CSV HEADER;

COPY si_gurs_kn_ds 
FROM '/csvs/si_gurs_kn_ds.csv' 
DELIMITER ',' 
CSV HEADER;

COPY points 
FROM '/csvs/points.csv' 
DELIMITER ',' 
CSV HEADER;

COPY omarice_api 
FROM '/csvs/omarice_api.csv' 
DELIMITER ',' 
CSV HEADER;

CREATE INDEX IF NOT EXISTS idx_hs_eid ON si_gurs_kn_slo_hisne_st(eid_hisna_stevilka);
CREATE INDEX IF NOT EXISTS idx_ds_eid ON si_gurs_kn_ds(eid_hisna_stevilka);
CREATE INDEX IF NOT EXISTS idx_points_eid ON points(eid_hisna_stevilka_key);
CREATE INDEX IF NOT EXISTS idx_points_type ON points(point_type_id);
CREATE INDEX IF NOT EXISTS idx_omarice_jasek ON omarice_api(idjasek);
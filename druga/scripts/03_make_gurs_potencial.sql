WITH apartment_counts AS (
    SELECT 
        eid_hisna_stevilka,
        COUNT(*) as total_count
    FROM si_gurs_kn_ds
    WHERE vrsta_dejanske_rabe_del_st_id IN (
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 19, 
        21, 22, 23, 24, 25, 26, 42, 43, 44, 47, 48, 49, 
        50, 52, 53
    )
    GROUP BY eid_hisna_stevilka
)
UPDATE si_gurs_kn_slo_hisne_st
SET gurs_potencial = apartment_counts.total_count
FROM apartment_counts
WHERE si_gurs_kn_slo_hisne_st.eid_hisna_stevilka = apartment_counts.eid_hisna_stevilka;
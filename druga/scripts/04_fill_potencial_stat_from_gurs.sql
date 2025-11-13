UPDATE points p
SET potencial_stat = hs.gurs_potencial
FROM si_gurs_kn_slo_hisne_st hs
WHERE p.eid_hisna_stevilka_key = hs.eid_hisna_stevilka
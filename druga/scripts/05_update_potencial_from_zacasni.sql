UPDATE points p
SET potencial_stat = FLOOR(p.zacasni_potencial)
FROM omarice_api o
WHERE p.old_id = o.idjasek
  AND o.idstatusomara IN (1, 3)
  AND p.eid_hisna_stevilka_key IS NOT NULL
  AND (p.zacasni_potencial IS NOT NULL)
  AND (p.potencial_stat IS NULL);
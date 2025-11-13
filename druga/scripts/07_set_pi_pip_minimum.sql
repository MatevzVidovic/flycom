UPDATE points p
SET potencial_stat = 1
FROM omarice_api o
WHERE p.old_id = o.idjasek
  AND o.idstatusomara IN (1, 3)
  AND p.potencial_stat = 0;
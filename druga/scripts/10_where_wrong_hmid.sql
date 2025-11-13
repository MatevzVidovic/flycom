UPDATE points
SET potencial_stat = FLOOR(zacasni_potencial)
WHERE napacen_hmid = '1.0'
  AND (zacasni_potencial IS NOT NULL);
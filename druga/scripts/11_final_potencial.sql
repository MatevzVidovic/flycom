UPDATE points
SET potencial_stat = FLOOR(pravi_potencial)
WHERE pravi_potencial IS NOT NULL;

WITH multiple_point_counts AS (
    SELECT 
        p.eid_hisna_stevilka_key,
        COUNT(*) as point_count,
        SUM(potencial_stat) as total_potencial
    FROM points p
    JOIN omarice_api o ON p.old_id = o.idjasek
    WHERE o.idstatusomara IN (1, 3)
      AND p.eid_hisna_stevilka_key IS NOT NULL
    GROUP BY p.eid_hisna_stevilka_key
    HAVING COUNT(*) > 1
)
UPDATE points p
SET potencial_stat = FLOOR(mpc.total_potencial / mpc.point_count)
FROM multiple_point_counts mpc
WHERE p.eid_hisna_stevilka_key = mpc.eid_hisna_stevilka_key
  AND FLOOR(mpc.total_potencial / mpc.point_count) > 0;
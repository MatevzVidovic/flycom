


"""
•	Tabele v bazi naj imajo vsaj naslednje stolpce:
o	si_gurs_kn_slo_hisne_st: eid_hisna_stevilka, gurs_potencial
o	si_gurs_kn_ds: eid_hisna_stevilka, vrsta_dejanske_rabe_del_st_id
o	points: id, eid_hisna_stevilka_key, old_id, potencial_stat, zacasni_potencial, pravi_potencial, napacen_hmid, point_type_id
o	omarice_api: idjasek, idstatusomara
"""

import pandas as pd




# Exploration section

if False:
    hs = pd.read_csv("./druga_data/original_data/KN_SLO_NASLOVI_HS_naslovi_hs_20251109.csv")
    print(hs)

    ds = pd.read_csv("./druga_data/original_data/KN_SLO_STAVBE_SLO_deli_stavb_20251109.csv")
    print(ds)


    points = pd.read_csv("./druga_data/original_data/points.csv")
    print(points)

    omarice_api = pd.read_csv("./druga_data/original_data/omarice_api.csv")
    print(omarice_api)

    print(hs.columns)
    print(ds.columns)
    print(points.columns)
    print(omarice_api.columns)




# Excecution section


hs = pd.read_csv("./druga_data/original_data/KN_SLO_NASLOVI_HS_naslovi_hs_20251109.csv",  
                 usecols=["EID_HISNA_STEVILKA"],
                 dtype={"EID_HISNA_STEVILKA": "Int64"})
hs = hs.rename(columns={"EID_HISNA_STEVILKA" : "eid_hisna_stevilka"})
hs["gurs_potencial"] = 0
print(hs)
hs = hs.dropna(subset=['eid_hisna_stevilka'])
print(hs)
hs = hs.drop_duplicates(subset='eid_hisna_stevilka', keep='first')
print(hs)
# hs = hs.dropna()
# print(hs)


ds = pd.read_csv("./druga_data/original_data/KN_SLO_STAVBE_SLO_deli_stavb_20251109.csv",  
                 usecols=["EID_HISNA_STEVILKA", "VRSTA_DEJANSKE_RABE_DEL_ST_ID"],
                 dtype={"EID_HISNA_STEVILKA": "Int64"})
ds = ds.rename(columns={"EID_HISNA_STEVILKA" : "eid_hisna_stevilka", "VRSTA_DEJANSKE_RABE_DEL_ST_ID" : "vrsta_dejanske_rabe_del_st_id"})
print(ds)
ds = ds.dropna(subset=['eid_hisna_stevilka']) # Found no Nan
print(ds)
# ds = ds.dropna()
# print(ds)


points = pd.read_csv("./druga_data/original_data/points.csv",  
                    usecols=["id", "eid_hisna_stevilka_key", "old_id", "potencial_stat", "zacasni_potencial", "pravi_potencial", "napacen_hmid", "point_type_id"],
                    dtype={"eid_hisna_stevilka_key": "Int64"}) #, "potencial_stat": "Int64", "zacasni_potencial": "Int64"})
print(points)
# points = points.dropna()
# print(points)

omarice_api = pd.read_csv("./druga_data/original_data/omarice_api.csv",  usecols=["idjasek", "idstatusomara"])
print(omarice_api)
# omarice_api = omarice_api.dropna() # Found no Nan
# print(omarice_api)



print(hs.columns)
print(ds.columns)
print(points.columns)
print(omarice_api.columns)


hs.to_csv("druga_data/simplified_data/si_gurs_kn_slo_hisne_st.csv", index=False)
ds.to_csv("druga_data/simplified_data/si_gurs_kn_ds.csv", index=False)
points.to_csv("druga_data/simplified_data/points.csv", index=False)
omarice_api.to_csv("druga_data/simplified_data/omarice_api.csv", index=False)
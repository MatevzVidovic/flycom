


# with open("druga_data/original_data/KN_SLO_NASLOVI_HS_naslovi_hs_20251109.csv") as f:
#     text = f.read()
#     print(text.split("\n")[0:10])


with open("druga_data/original_data/KN_SLO_STAVBE_SLO_deli_stavb_20251109.csv") as f:
    text = f.read()
    [print(i) for i in text.split("\n")[1000:1010]]
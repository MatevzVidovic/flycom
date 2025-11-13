
import os
import shutil as sh
import pandas as pd




# df = pd.read_csv("./testni_dan_matevz/testni_dan_matevz/priloge_naloga_1/pp_kp_trans.csv", sep=',', header='infer', usecols=["dat_pri", "datum_prve_uveljavitve_posla"])
df = pd.read_csv("./prva_data/pp_kp_trans.csv", sep=',', header='infer', usecols=["dat_pri", "datum_prve_uveljavitve_posla"])
print(df)



df = df.dropna(subset=["dat_pri", "datum_prve_uveljavitve_posla"])
df = df.reset_index()
df["dp"] = df["dat_pri"]
df["dpup"] = df["datum_prve_uveljavitve_posla"]

print(df)
df.drop("dat_pri", inplace=True, axis=1)
df.drop("datum_prve_uveljavitve_posla", inplace=True, axis=1)
print(df)



# df["dp"], df["dpup"] = df["dp"].drop("nan"), df["dpup"].drop("nan")
# print(df)


print(type(df["dp"][100]))
print(df["dp"][100])
print(df["dp"][100].split("-"))


# os.exit(0)

def extract_year(s: str) -> str:
    if isinstance(s, str):
        return s.split("-")[0]
    else:
        print(s)
        return None

df["dp"], df["dpup"] = df["dp"].apply(extract_year), df["dpup"].apply(extract_year)
print(df)



# Group by dp, select (dp, count(dp == dpus) as on_time, count(dp < dpus) as later, count(dp > dpus) as earlier)
# - order by dp
# - assert  earlier == 0
# - create col coef, is (later / (on_time / later))

agg = df.groupby('dp').apply(lambda g: pd.Series({
    'on_time': (g['dp'] == g['dpup']).sum(),
    'later': (g['dp'] < g['dpup']).sum(),
    'earlier': (g['dp'] > g['dpup']).sum()
})).reset_index().sort_values('dp')

print(agg)


agg = agg.astype(int)

last_year = agg.query('dp == 2025')
agg = agg.query('dp >= 2015 and dp < 2025')

print(last_year)
print(agg)


agg["coef"] = agg["later"] / (agg["later"] + agg["on_time"])
print(agg)

os.makedirs("prva_data", exist_ok=True)

avg_coef = agg["coef"].mean()
print(avg_coef)
with open("prva_data/avg_coef.txt", mode="w") as f:
    f.write(str(avg_coef))

last_year.to_csv("prva_data/last_year.csv", index=False)
agg.to_csv("prva_data/previous_years.csv", index=False)
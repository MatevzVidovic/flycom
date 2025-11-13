
import pandas as pd

with open("prva_data/avg_coef.txt") as f:
    txt = f.read()
    coef = float(txt)

print(coef)


df = pd.read_csv("./prva_data/last_year.csv")
print(df)

expected = df["on_time"][0] * coef

with open("prva_data/pred.txt", 'w') as f:
    f.write(str(int(expected)))

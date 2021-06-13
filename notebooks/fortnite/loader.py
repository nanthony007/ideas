import pandas as pd
import json

with open("teams.json", "r", encoding="utf-8") as f:
    teams = json.load(f)

df = pd.DataFrame.from_records(teams.get("results"))
print(df.columns)
print(df.shape)
df.to_csv("teams.csv", index=False)

df.to_csv("fkasn", index=False)

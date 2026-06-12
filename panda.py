import pandas as pd

df = pd.DataFrame({
    "Price": [100,110,120,150]
})
df["MA2"] = df["Price"].rolling(2).mean()
df["MA3"] = df["Price"].rolling(3).mean()

df["Signal"] = 0
df.loc[2,"Price"]
df.loc[df["MA2"] > df["MA3"], "Signal"] = 1
df.loc()
print(df)
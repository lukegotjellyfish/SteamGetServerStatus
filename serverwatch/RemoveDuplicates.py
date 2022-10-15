from functools import reduce
import pandas as pd


df = reduce(
    lambda df_i, df_j: pd.concat([df_i, df_j]).drop_duplicates(subset=["Date", "Time"]),
    pd.read_csv("Output.csv", chunksize=100000)
)
df.to_csv("ServerWatch.csv")
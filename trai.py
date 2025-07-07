import pandas as pd


data = pd.read_csv(r"E:\ML_OPS\DVC_experments\DVC\test.csv")
# print(data)

data["x"] = 2*data["x"]

data.to_csv("test.csv" , index=False)



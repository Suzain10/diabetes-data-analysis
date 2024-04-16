import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("diabetes.csv")
profile = ProfileReport(df)
profile.to_file("Diabetes.html")

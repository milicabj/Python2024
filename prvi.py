import pandas as pd

df=pd.read_csv("Dataset .csv")


maks=df['Average Cost for two'].max()
minn =df['Average Cost for two'].min()


print(maks)
print(minn)

prosjek = df['Average Cost for two'].mean()
print(prosjek)

proc_razlika = (maks - prosjek)/ 100
print(proc_razlika)

#normalizovan_df=(df['Average Cost for two']-df['Average Cost for two'].mean())/df['Average Cost for two'].std()

normalizovan_df=(df['Average Cost for two']-df['Average Cost for two'].min())/(df['Average Cost for two'].max()-df['Average Cost for two'].min())
print(normalizovan_df)
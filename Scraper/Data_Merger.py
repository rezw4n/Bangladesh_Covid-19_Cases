import pandas as pd


pop_data = pd.read_csv('../Data/district_wise_population(2016).csv')
pop_data.columns = list(map(lambda x: x.lower(), pop_data.columns))
df = pd.read_csv("../Data/district_cases.csv")
merged_df = df.merge(pop_data, how='inner', on = 'district')
merged_df.set_index('district')
merged_df.to_csv('../Data/cases_including_pop_data.csv')
merged_df.to_pickle('../Data/cases_including_pop_data.pkl')

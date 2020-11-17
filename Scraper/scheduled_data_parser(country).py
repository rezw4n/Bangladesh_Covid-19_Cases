import pandas as pd
import pickle

df = pd.read_csv('https://covid19.who.int/WHO-COVID-19-global-data.csv')


def data_updater(dataframe):
    df.columns = df.columns.str.strip().str.lower()
    df.drop(labels=['country_code', 'who_region'], axis=1, inplace=True)
    country_group = df.groupby(by='country')
    bd = country_group.get_group('Bangladesh')
    nan_indexes = bd[bd['cumulative_cases'] == 0].index
    bd_daily_cases = bd.drop(index=nan_indexes)
    bd_daily_cases.set_index('date_reported', inplace=True)
    with open('bd_daily_cases.pkl', 'wb') as output_file:
        return pickle.dump(bd_daily_cases, output_file), bd_daily_cases.to_csv('bd_daily_cases.csv')


data_updater(df)

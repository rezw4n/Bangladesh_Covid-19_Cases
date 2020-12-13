import pandas as pd


dataframe = pd.read_html(
    'https://docs.google.com/spreadsheets/d/e/2PACX-1vQgQAWwlQYF4XTxVT8sYP5wwqz_KxaWfVNQk9B0FlyPPpDphAIv1cRIMV4ve_1gNbewGjcbkKNpi3Wm/pub?gid=624602850&#')[
    1]


def district_data_updater(df):
    df.columns = df.loc[1]
    dhaka = {
        'District/City': 'Dhaka',
        'Total No of Cases': int(df.loc[2]['Total No of Cases']) + int(df.loc[3]['Total No of Cases'])
    }

    df = df.append(dhaka, ignore_index=True)
    df.drop(index=[0, 1], inplace=True)
    df.drop(labels=[2, 'Division'], axis=1, inplace=True)
    df.dropna(axis=1, how='all', inplace=True)
    df.dropna(how='any', inplace=True)
    df.drop(labels=[2, 3], inplace=True)
    changed_district_name = {
        "Coxâs bazar": "Cox's Bazar",
        "B. Baria": "Brahmanbaria",
        "Jessore": "Jashore",
        "Munshigonj": "Munshiganj",
        "Laksmipur": "Lakshmipur",
    }
    df['District/City'] = df['District/City'].map(changed_district_name).fillna(df['District/City'])
    df['Total No of Cases'] = df['Total No of Cases'].astype(int)
    df.sort_values(by='Total No of Cases', ascending=False, inplace=True)
    df.columns = ['district', 'total_cases']
    # df.rename(columns={"District/City": "district", "Total No of Cases": "total_cases"}, inplace=True)
    df.set_index('district', inplace=True)
    return df.to_pickle('../Data/district_cases.pkl'), df.to_csv('../Data/district_cases.csv')


district_data_updater(dataframe)

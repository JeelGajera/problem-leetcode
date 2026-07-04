import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:

    df = person.merge(address, on="personId", how="left")
    df.drop(columns=['personId', 'addressId'],inplace=True)
    return df
import pandas as pd


def merge_data(
    df1: pd.DataFrame,
    df2: pd.DataFrame,
    left_on: str = None,
    right_on: str = None,
    on: str = None,
    how: str = "inner",
) -> pd.DataFrame:

    if on:
        merged_df = pd.merge(df1, df2, on=on, how=how)
    else:
        # Caso contrário, utiliza 'left_on' e 'right_on'
        merged_df = pd.merge(df1, df2, left_on=left_on, right_on=right_on, how=how)

    return merged_df
